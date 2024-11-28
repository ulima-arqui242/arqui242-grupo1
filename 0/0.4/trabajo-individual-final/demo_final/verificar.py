import sqlite3

conn = sqlite3.connect('test.db')
cursor = conn.cursor()

cursor.execute("SELECT COUNT(*) FROM Employees")
print(f"Registros en Employees: {cursor.fetchone()[0]}")

cursor.execute("SELECT COUNT(*) FROM Customers")
print(f"Registros en Customers: {cursor.fetchone()[0]}")

cursor.execute("SELECT COUNT(*) FROM Products")
print(f"Registros en Products: {cursor.fetchone()[0]}")

conn.close()
