from agent import Agent
from db_init import create_db
import sqlite3

class SQL_to_DB_Agent(Agent):
    def __init__(self, path):
        super().__init__("SQL to DB Agent")
        _, path = create_db()
        self.db_path = path

    def process(self, sql_query):
        try:
            # Connetti al database
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            # Esegui la query nel database
            cursor.execute(sql_query)
            result = cursor.fetchall()
            #print("Raw results:", result)  # Debug statement to check raw results
            return result, cursor

        except Exception as e:
            print(f"Error executing the query: {e}")
        finally:
            conn.close()