import sqlite3
import os

def create_db():

    db_path = 'employees.db'
    # Remove the old database if it exists
    if os.path.exists(db_path):
        os.remove(db_path)
    conn = sqlite3.connect('employees.db')
    # Create a cursor object to execute SQL commands
    cursor = conn.cursor()

# Create the departments table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS departments (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL
    )
    ''')

    # Create the employees table with department_id as a foreign key
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS employees (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        department_id INTEGER NOT NULL,
        join_date TEXT NOT NULL,
        salary REAL NOT NULL,
        FOREIGN KEY (department_id) REFERENCES departments(id)
    )
    ''')

    conn.commit()

    # Insert some sample data into the departments table
    cursor.execute('''
    INSERT INTO departments (name)
    VALUES
        ('Marketing'),
        ('Engineering'),
        ('Sales'),
        ('HR')
    ''')

    # Insert sample data into the employees table with department_id
    cursor.execute('''
    INSERT INTO employees (name, department_id, join_date, salary)
    VALUES
        ('John Doe', 1, '2021-06-15', 55000),
        ('Jane Smith', 2, '2020-03-01', 75000),
        ('Mike Johnson', 3, '2019-11-20', 62000),
        ('Emily Davis', 4, '2022-08-25', 48000),
        ('Robert Brown', 2, '2018-09-10', 88000)
    ''')

    conn.commit()

    # Fetch and display the data to confirm the insertion
    cursor.execute('SELECT * FROM employees')
    rows = cursor.fetchall()

    #for row in rows:   #for debugging
        #print(row) 

    # Close the connection
    conn.close()

    db_schema = "There are 2 tables in this DB. The first one is 'departments' which contains the following columns: id (INTEGER): Primary key, uniquely identifies each department, and 'name'(column name) (TEXT): which contains the name of the department. The second table is 'employees' where we can find the following columns: id (INTEGER): Primary key, uniquely identifies each employee. name (TEXT): The full name of the employee. department_id (INTEGER): Foreign key referencing the id in the departments table, indicating the employee's department. join_date (TEXT): The date the employee joined the company. salary (REAL): The salary of the employee."
    
    return db_schema, db_path