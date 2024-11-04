from agent import Agent
from db_init import create_db
from langchain_community.utilities.sql_database import SQLDatabase
from langchain_openai import ChatOpenAI
from langchain_community.agent_toolkits.sql.toolkit import SQLDatabaseToolkit


class nl_to_sql_Agent(Agent):
    def __init__ (self):
        super().__init__("NL to SQL Agent")
    def process(self, user_input):
        llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.5, api_key="INSERT YOUR KEY")
        prompt = f"{create_db}\nConvert this from natural language into a SQL query: {user_input}. Only give me SQL as an answer."
        sql_query = llm.invoke(prompt)
        sql_query = sql_query.content.strip()
        sql_query = sql_query.replace('```sql', '').replace('```', '').strip()  # Remove formatting

        return sql_query