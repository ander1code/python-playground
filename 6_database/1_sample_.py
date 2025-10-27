
import sqlite3
import os

database = "dbcrud.db"

if os.path.exists(database):
    os.remove(database)
    flag = True

cursor = sqlite3.connect(database).cursor()
cursor.execute("CREATE TABLE PERSON (ID INTEGER PRIMARY KEY AUTOINCREMENT, NAME VARCHAR(45) NOT NULL, SALARY DECIMAL(12,2) NOT NULL);")
cursor.connection.commit()

people_list = [
    ("Anderson", 2152.11),
    ("Beatriz", 3275.40),
    ("Carlos", 1890.75),
    ("Daniela", 4520.00),
    ("Eduardo", 3010.30),
    ("Fernanda", 2780.90),
    ("Gabriel", 2335.50),
    ("Helena", 3900.25),
    ("Igor", 2100.00),
    ("Juliana", 4999.99),
    ("Kleber", 1875.60),
    ("Larissa", 3300.00),
    ("Marcelo", 2700.15),
    ("Natália", 4120.80),
    ("Otávio", 3640.45),
    ("Patrícia", 2215.33),
    ("Ricardo", 3185.77),
    ("Sabrina", 2950.22),
    ("Thiago", 4050.10),
    ("Vanessa", 3888.88)
]

cursor.executemany("INSERT INTO PERSON (NAME, SALARY) VALUES (?,?)",people_list)
cursor.connection.commit()

people = cursor.execute("SELECT * FROM PERSON").fetchall()
for p in people:
    print(f"ID: {p[0]} | NAME: {p[1]} | SALARY: {p[2]}")


people = cursor.execute("SELECT * FROM PERSON WHERE NAME LIKE ?", ("A%",)).fetchall()
for p in people:
    print(f"ID: {p[0]} | NAME: {p[1]} | SALARY: {p[2]}")

cursor.execute("UPDATE PERSON SET NAME = ?, SALARY = ? WHERE ID = ?", ("Anderson C.", 7821.11, 1))
cursor.connection.commit()

person = cursor.execute("SELECT * FROM PERSON WHERE ID = ?", (1,)).fetchone()
print(f"ID: {person[0]} | NAME: {person[1]} | SALARY: {person[2]}")

cursor.execute("DELETE FROM PERSON WHERE ID = ?", (1,))
cursor.connection.commit()

people = cursor.execute("SELECT * FROM PERSON WHERE NAME LIKE ?", ("A%",)).fetchall()
if len(people) == 0:
    print("person not registered.")

cursor.close()

