import mysql.connector

class Crud:
    def __init__(self):
      self.__conn = None
      self.__create_table()

    def __get_cursor(self):
       try:
         self.__conn = mysql.connector.connect(
            host="localhost",
            database="dbreview",
            user="root",
            passwd="121181"
         )
         return self.__conn.cursor()  
       except Exception:
         print("Error cursor creating.")
         return None
       
    def __create_table(self):
       try:
         stmt = self.__get_cursor()
         stmt.execute("DROP TABLE IF EXISTS PERSON")
         stmt.execute("CREATE TABLE PERSON(ID INTEGER PRIMARY KEY, NAME CHAR(100) NOT NULL);")
         stmt._connection.commit()
         stmt.close()
         self.__conn.close()
         print("Sucessfully table created.")
         return True
       except Exception:
         print("Error table creating.")
         return False
       
    def create_person(self, id, name):
       try:
         stmt = self.__get_cursor()
         stmt.execute("INSERT INTO PERSON (ID, NAME) VALUES (%s, %s);", (id, name, ))
         stmt._connection.commit()
         print("Sucessfully person created.")
         stmt.close()
         self.__conn.close()
         return True
       except Exception:
         print("Error person creating.")
         return False
       
    def update_person(self, id, name):
       try:
         stmt = self.__get_cursor()
         stmt.execute(f"UPDATE PERSON SET NAME = '{name}' WHERE ID = {id}")
         stmt._connection.commit()
         print("Sucessfully updated.")
         stmt.close()
         self.__conn.close()
         return True
       except Exception:
         print("Error person updating.")
         return False
       
    def delete_person(self, id):
       try:
         stmt = self.__get_cursor()
         stmt.execute("DELETE FROM PERSON WHERE ID = %s", (id, ))
         stmt._connection.commit()
         print("Sucessfully deleted.")
         stmt.close()
         self.__conn.close()
         return True
       except Exception:
         print("Error person deleting.")
         return False
       
    def get_person_by_name(self, name):
       try:
        stmt = self.__get_cursor()
        stmt.execute("SELECT * FROM PERSON WHERE NAME LIKE %s", (name + "%", ))
        people = stmt.fetchall()
        if len(people) == 0:
            print("Nothing!")
        else:
            for person in people:
                print(person)
        stmt.close()
        self.__conn.close()
       except Exception:
        print("Error person getting by name.")
        return False
       
    def get_person_by_id(self, id):
       try:
        stmt = self.__get_cursor()
        stmt.execute(f"SELECT * FROM PERSON WHERE ID = {id}")
        for person in stmt.fetchone():
           print(person)
        stmt.close()
        self.__conn.close()
       except Exception:
        print("Error person getting by id.")
        return False

    def __enter__(self):
       return self
       
    def __exit__(self, v1, v2, v3):
       pass

def execute_example_02():
    with Crud() as crud:
        crud.create_person(123, "Anderson")
        crud.get_person_by_name("A")
        crud.update_person(123, "Anderson C.")
        crud.get_person_by_id(123)
        crud.delete_person(123)
        crud.get_person_by_name("")

execute_example_02()