from nl_to_sql import nl_to_sql_Agent
from query_validator import QueryValidator
from result_formatter import Result_Formatting_Agent
from sql_to_db import SQL_to_DB_Agent

def main(user_input):
    # Agents
    nl_to_sql_agent = nl_to_sql_Agent()
    query_validator_agent = QueryValidator()
    sql_to_db_agent = SQL_to_DB_Agent('employees.db')
    result_formatter_agent = Result_Formatting_Agent()

    # Process input through agents
    sql_query = nl_to_sql_agent.process(user_input)
    print(f"SQL Query: {sql_query}")
    
    is_valid, validation_msg = query_validator_agent.process(sql_query)
    if not is_valid:
        return f"Query Validation Failed: {validation_msg}"

    result, cursor = sql_to_db_agent.process(sql_query)
    if result is None:
        return "Error executing the query."

    final_table = result_formatter_agent.process(result, cursor)
    return final_table

# Example usage
schema_db = 'There are 2 tables in this DB. The first one is "departments" which contains the following columns: id (INTEGER): Primary key, uniquely identifies each department, and name (TEXT): which contains the name of the department. The second table is "employees" where we can find the following columns: id (INTEGER): Primary key, uniquely identifies each employee. name (TEXT): The full name of the employee. department_id (INTEGER): Foreign key referencing the id in the departments table, indicating the employee"s department. join_date (TEXT): The date the employee joined the company. salary (REAL): The salary of the employee.'
user_input = f"{schema_db} Given my DB_Schema, Tell me the average salary for each department"
print(main(user_input))