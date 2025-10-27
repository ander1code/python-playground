import mysql.connector

def execute_example_01():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            database="dbreview",
            user="root",
            passwd="121181"
        )
        conn.autocommit = False
        cursor = conn.cursor()
        print("Sucessfully connected.")

        cursor.execute("DROP TABLE IF EXISTS PERSON;")
        cursor.execute("CREATE TABLE PERSON(ID INTEGER, NAME VARCHAR(100) NOT NULL);")
        cursor._connection.commit()
        print("Sucessfully table created.")

        sql = "INSERT INTO PERSON (ID , NAME) VALUES (%s, %s);"
        values = (123, "Anderson")
        cursor.execute(sql, values)
        cursor._connection.commit()
        print("Sucessfully inserted.")

        values = [(321,"Sara"),(432, "Mara"),(654, "Luiza"),(876, "Fernanda"),(821, "Renata"),(984, "Caroline")]
        cursor.executemany(sql, values)
        cursor._connection.commit()
        print("Sucessfully MANY inserteds.")

        cursor.execute("SELECT * FROM PERSON WHERE NAME LIKE %s;", ("A%", ))
        people = cursor.fetchall()
        for person in people:
            print(person)

        cursor.execute(f"UPDATE PERSON SET NAME = '{"Anderson C."}' WHERE ID = {123};")
        cursor._connection.commit()
        print("Sucessfully updated.")

        cursor.execute("SELECT * FROM PERSON WHERE ID = %s;", (123, ))
        print(cursor.fetchone())

        cursor.execute(f"DELETE FROM PERSON WHERE ID = {123};")
        cursor._connection.commit()
        print("Sucessfully deleted.")

        cursor.execute("SELECT * FROM PERSON ORDER BY NAME ASC;")
        people = cursor.fetchall()
        for person in people:
            print(person)

        cursor.close()
        conn.close()
    except Exception:
        print("Error executing.")

execute_example_01()