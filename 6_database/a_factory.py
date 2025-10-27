import sqlite3

class ConnectionFactory:
    __cursor = None

    def __new__(cls, *args, **kwargs):
        if cls.__cursor is None:
            print("Creating connection...")
            cls.__cursor = sqlite3.connect("dbcrud.db").cursor()
            print("Created.")
        else:
            print("Connection already created.")
        return cls.__cursor

cursor1 = ConnectionFactory()
cursor2 = ConnectionFactory()
print(f"id(cursor1) == id(cursor2) = {id(cursor1) == id(cursor2)}")
for i in range(0,10):
    print(ConnectionFactory())



