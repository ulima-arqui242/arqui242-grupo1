from locust import User, task, between
import sqlite3
from faker import Faker

# Instancia de Faker para generar datos sintéticos
fake = Faker()

class SQLiteLoadTest(User):
    wait_time = between(1, 3)  # Tiempo de espera entre tareas (en segundos)

    def on_start(self):
        """Se ejecuta al iniciar cada usuario simulado."""
        self.conn = sqlite3.connect("test.db")  # Conecta a la base de datos
        self.cursor = self.conn.cursor()

    def on_stop(self):
        """Se ejecuta al detener cada usuario simulado."""
        self.conn.close()  # Cierra la conexión a la base de datos

    @task(2)  # Tarea con un peso de 2 (se ejecuta más frecuentemente)
    def insert_employee(self):
        """Inserta un registro en la tabla Employees."""
        self.cursor.execute("""
        INSERT INTO Employees (LastName, FirstName, "Address", City, "State", Country, Phone)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            fake.last_name(),
            fake.first_name(),
            fake.street_address(),
            fake.city(),
            fake.state(),
            fake.country(),
            fake.phone_number()
        ))
        self.conn.commit()

    @task(1)  # Tarea con un peso de 1 (se ejecuta menos frecuentemente)
    def insert_customer(self):
        """Inserta un registro en la tabla Customers."""
        self.cursor.execute("""
        INSERT INTO Customers (LastName, FirstName, "Address", City, Country, Email, CreditCard)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            fake.last_name(),
            fake.first_name(),
            fake.street_address(),
            fake.city(),
            fake.country(),
            fake.email(),
            fake.credit_card_number()
        ))
        self.conn.commit()

    @task(1)
    def insert_product(self):
        """Inserta un registro en la tabla Products."""
        self.cursor.execute("""
        INSERT INTO Products (ProductName, UnitPrice)
        VALUES (?, ?)
        """, (
            fake.word().capitalize(),
            fake.random_int(min=10, max=170)
        ))
        self.conn.commit()
