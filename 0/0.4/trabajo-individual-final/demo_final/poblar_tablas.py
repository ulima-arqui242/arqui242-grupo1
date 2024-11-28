from faker import Faker
import sqlite3
from random import randint

# Instancia de Faker
fake = Faker()

# Conectar a la base de datos
conn = sqlite3.connect('test.db')
cursor = conn.cursor()

# Poblar tabla Employees
print("Poblando tabla 'Employees'...")
for _ in range(50):  
    last_name = fake.last_name()
    first_name = fake.first_name()
    address = fake.street_address()
    city = fake.city()
    state = fake.state()
    country = fake.country()
    phone = fake.phone_number()

    cursor.execute("""
    INSERT INTO Employees (LastName, FirstName, "Address", City, "State", Country, Phone)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (last_name, first_name, address, city, state, country, phone))

# Poblar tabla Customers
print("Poblando tabla 'Customers'...")
for _ in range(50):  
    last_name = fake.last_name()
    first_name = fake.first_name()
    address = fake.street_address()
    city = fake.city()
    country = fake.country()
    email = fake.email()
    credit_card = fake.credit_card_number() 

    cursor.execute("""
    INSERT INTO Customers (LastName, FirstName, "Address", City, Country, Email, CreditCard)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (last_name, first_name, address, city, country, email, credit_card))

# Poblar tabla Products
print("Poblando tabla 'Products'...")
for _ in range(50):  
    product_name = fake.word().capitalize()  
    unit_price = fake.random_int(min=10, max=170)

    cursor.execute("""
    INSERT INTO Products (ProductName, UnitPrice)
    VALUES (?, ?)
    """, (product_name, f"{unit_price:.2f}"))

# Confirmar cambios y cerrar conexión
conn.commit()
conn.close()

print("Datos generados y tablas pobladas con éxito.")
