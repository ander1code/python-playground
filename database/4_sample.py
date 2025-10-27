import sqlite3
import os
import sys

database = "dbCrud.db"

try:
    if os.path.exists(database):
        os.remove(database)

    conn = sqlite3.connect(database)
    cursor = conn.cursor()

    try:
        cursor.execute("""
            CREATE TABLE Person (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                NAME VARCHAR(45) NOT NULL
            )
        """)
        conn.commit()

        cursor.execute("INSERT INTO PERSON (NAME) VALUES('Anderson')")
        conn.commit()

        people = cursor.execute("SELECT * FROM PERSON WHERE NAME LIKE 'A%'")
        for p in people:
            print(p)

        cursor.execute("UPDATE PERSON SET NAME = 'Anderson Conceição' WHERE ID = 1")
        conn.commit()

        person = cursor.execute("SELECT * FROM PERSON WHERE ID = 1").fetchone()
        print(person)

        cursor.execute("DELETE FROM PERSON WHERE ID = 1")
        conn.commit()

        people = cursor.execute("SELECT * FROM PERSON WHERE NAME LIKE 'A%'").fetchall()
        if not people:
            print("Empty table.")

    except Exception as err:
        print(f"Error: {err}")
        conn.rollback()
    finally:
        conn.close()

except Exception as err:
    print(f"Error: {err}")

sys.exit()
