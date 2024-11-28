import sqlite3
from faker import Faker
from multiprocessing import Pool

# Configuración global
fake = Faker()
DB_FILE = 'test.db'
BATCH_SIZE = 1000  # Tamaño de cada lote
PROCESSES = 4      # Número de procesos paralelos


# Función para insertar datos en la tabla Employees
def insert_employees(data_batch):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.executemany("""
    INSERT INTO Employees (LastName, FirstName, "Address", City, "State", Country, Phone)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """, data_batch)
    conn.commit()
    conn.close()


# Función para insertar datos en la tabla Customers
def insert_customers(data_batch):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.executemany("""
    INSERT INTO Customers (LastName, FirstName, "Address", City, Country, Email, CreditCard)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """, data_batch)
    conn.commit()
    conn.close()


# Función para insertar datos en la tabla Products
def insert_products(data_batch):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.executemany("""
    INSERT INTO Products (ProductName, UnitPrice)
    VALUES (?, ?)
    """, data_batch)
    conn.commit()
    conn.close()


# Generador de datos para Employees
def generate_employees(n):
    data = []
    for _ in range(n):
        data.append((
            fake.last_name(),
            fake.first_name(),
            fake.street_address(),
            fake.city(),
            fake.state(),
            fake.country(),
            fake.phone_number()
        ))
    return data


# Generador de datos para Customers
def generate_customers(n):
    data = []
    for _ in range(n):
        data.append((
            fake.last_name(),
            fake.first_name(),
            fake.street_address(),
            fake.city(),
            fake.country(),
            fake.email(),
            fake.credit_card_number()
        ))
    return data


# Generador de datos para Products
def generate_products(n):
    data = []
    for _ in range(n):
        data.append((
            fake.word().capitalize(),
            f"{fake.random_int(min=10, max=170):.2f}"  # Precio entre 10 y 170
        ))
    return data


# Función para generar y poblar tablas masivamente
def generate_large_dataset(total_records, table, insert_function, generate_function):
    pool = Pool(PROCESSES)
    batches = total_records // BATCH_SIZE

    for _ in range(batches):
        data_batch = generate_function(BATCH_SIZE)
        pool.apply_async(insert_function, args=(data_batch,))

    pool.close()
    pool.join()


if __name__ == "__main__":
    TOTAL_RECORDS = 1050  # Generar n registros

    print("Generando datos masivos para Employees...")
    generate_large_dataset(TOTAL_RECORDS, "Employees", insert_employees, generate_employees)

    print("Generando datos masivos para Customers...")
    generate_large_dataset(TOTAL_RECORDS, "Customers", insert_customers, generate_customers)

    print("Generando datos masivos para Products...")
    generate_large_dataset(TOTAL_RECORDS, "Products", insert_products, generate_products)

    print("Datos generados exitosamente.")
