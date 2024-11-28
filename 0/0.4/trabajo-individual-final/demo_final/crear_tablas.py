import sqlite3

# Conectar a la base de datos
conn = sqlite3.connect('test.db')  # Cambiar por tu base de datos
cursor = conn.cursor()

# Crear tabla Employees
cursor.execute("""
CREATE TABLE IF NOT EXISTS Employees (
    LastName VARCHAR(255) NOT NULL,
    FirstName VARCHAR(255) NOT NULL,
    "Address" VARCHAR(255),
    City VARCHAR(255),
    "State" VARCHAR(255),
    Country VARCHAR(255),
    Phone VARCHAR(255)
)
""")

# Crear tabla Customers
cursor.execute("""
CREATE TABLE IF NOT EXISTS Customers (
    LastName VARCHAR(255) NOT NULL,
    FirstName VARCHAR(255) NOT NULL,
    "Address" VARCHAR(255),
    City VARCHAR(255),
    Country VARCHAR(255),
    Email VARCHAR(255),
    CreditCard VARCHAR(255)
)
""")

# Crear tabla Products
cursor.execute("""
CREATE TABLE IF NOT EXISTS Products (
    ProductName VARCHAR(255) NOT NULL,
    UnitPrice VARCHAR(255)
)
""")

conn.commit()
conn.close()
