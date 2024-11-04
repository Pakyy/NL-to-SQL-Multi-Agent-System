from prettytable import PrettyTable
from agent import Agent

class Result_Formatting_Agent(Agent):
    def __init__(self):
        super().__init__("Result Formatter Agent")

    def process(self, result, cursor):
        if not result:
            return "No results found."

        # Inizializza la tabella PrettyTable
        table = PrettyTable()

        # Ottiene i nomi delle colonne dal cursore
        columns = [desc[0] for desc in cursor.description]
        table.field_names = columns

        # Verifica le righe e il numero di valori
        if len(result) > 0:
            for row in result:
                if len(row) == len(columns):
                    table.add_row(row)
                else:
                    # Logga il problema per capire cosa sta succedendo
                    print(f"Riga malformattata: {row} (Numero di colonne previsto: {len(columns)})")
                    # Continua o gestisci l'errore come desideri
                    continue  # Ignora le righe malformattate

        return table    
