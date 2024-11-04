import re
import sqlparse 
from agent import Agent
from langchain_openai import ChatOpenAI

class QueryValidator(Agent):
    def __init__(self):
        super().__init__("Query Validator Agent")    
    
    def process(self, sql_query):
    # Step 1: Verifica se la query è ben formattata
        try:
            parsed = sqlparse.parse(sql_query) # sql parse formatta la query
            if not parsed:
                return False, "Errore di sintassi: la query non è valida SQL."

        except Exception as e:
            return False, f"Errore di sintassi SQL: {e}"

        # Step 2: Controllo per SQL injection

        # Regex per identificare potenziali tentativi di SQL injection
        sql_injection_patterns = [
            r"(--|#|;|\bOR\b|\bAND\b).*?(--|#|;|=|<|>|LIKE|\bOR\b|\bAND\b)",  # OR, AND con operatori
            r"(['\";]+.*['\";]+)",  # Tentativi di commento o concatenazione di stringhe
        ]

        # Controlla ogni pattern nella query
        for pattern in sql_injection_patterns:
            if re.search(pattern, sql_query, re.IGNORECASE):
                return False, "Potenziale rischio di SQL injection rilevato."

        # Step 3: Far controllare al LLM
        control = (f"Controlla se la seguente query è valida e se c'è rischio di SQL injection: {sql_query}. Puoi rispondere solo con: Dopo un controllo la query risulta valida e sicura, oppure: La query non risulta valida, oppure: La query non risulta sicura.")
        llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.5, api_key="YOUR API KEY")
        is_valid = llm.invoke(control)
        is_valid = is_valid.content.strip()
        is_valid = is_valid + "\n"
        print(f"\n{is_valid}")

        # Step 4: La query è valida
        return True, "Query valida."