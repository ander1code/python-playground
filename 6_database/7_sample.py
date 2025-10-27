from abc import ABC

class Person(ABC):

    def __init__(self, id, name):
        self._id = id
        self._name = name
   
    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, id):
        self._id = id
  
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name

class NaturalPerson(Person):

    def __init__(self, id, name, salary):
        super().__init__(id, name)
        self.__salary = salary

    @property
    def salary(self):
        return self.__salary
    
    @salary.setter
    def salary(self, salary):
        self.__salary = salary

    def __str__(self):
        return f"ID: {self._id} | NAME: {self._name} | SALARY: {self.__salary}"

people = [
    NaturalPerson(1, "Anderson", 6151.11),
    NaturalPerson(2, "Beatriz", 4820.50),
    NaturalPerson(3, "Carlos", 3275.20),
    NaturalPerson(4, "Daniela", 7120.75),
    NaturalPerson(5, "Eduardo", 2980.00),
    NaturalPerson(6, "Fernanda", 3999.90),
    NaturalPerson(7, "Gabriel", 4550.25),
    NaturalPerson(8, "Helena", 3800.00),
    NaturalPerson(9, "Igor", 2750.70),
    NaturalPerson(10, "Juliana", 6850.33),
    NaturalPerson(11, "Kleber", 3015.40),
    NaturalPerson(12, "Larissa", 5630.88),
    NaturalPerson(13, "Marcelo", 4460.20),
    NaturalPerson(14, "Natália", 6220.10),
    NaturalPerson(15, "Otávio", 3300.00),
    NaturalPerson(16, "Patrícia", 5890.65),
    NaturalPerson(17, "Ricardo", 4785.77),
    NaturalPerson(18, "Sabrina", 3950.00),
    NaturalPerson(19, "Thiago", 7050.10),
    NaturalPerson(20, "Vanessa", 3888.88),
    NaturalPerson(21, "Wesley", 3120.22),
    NaturalPerson(22, "Yasmin", 4710.49),
    NaturalPerson(23, "Zeca", 2500.00),
    NaturalPerson(24, "Bruna", 5290.70),
    NaturalPerson(25, "Murilo", 3640.40),
    NaturalPerson(26, "Amanda", 6200.00),
    NaturalPerson(27, "Caio", 4100.25),
    NaturalPerson(28, "Débora", 3990.90),
    NaturalPerson(29, "Fábio", 3420.35),
    NaturalPerson(30, "Isabela", 4500.00)
]

import sys
import sqlite3
import os

database = "dbcrud.db"

class ConnectionFactory(object):
    __instance = None
    __cont = 0

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super(ConnectionFactory, cls).__new__(cls)
            cls.__cont += 1
        return cls.__instance

    def __init__(self):
        if not hasattr(self, "_initialized"):
            print(ConnectionFactory.__cont)
            self.__conn = sqlite3.connect(database)
            self.__cursor = self.__conn.cursor()
            self._initialized = True

    def get_cursor(self):
        return self.__cursor

    def get_connection(self):
        return self.__conn


class Crud(object):
    __instance = None
    __cont = 0

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super(Crud, cls).__new__(cls)
            cls.__cont += 1
        return cls.__instance

    def __init__(self):
        if not hasattr(self, "_initialized"):
            conn_factory = ConnectionFactory()
            self.__cursor = conn_factory.get_cursor()
            self.__conn = conn_factory.get_connection()
            self.__create_table()
            self._initialized = True

    def __create_table(self):
        try:
            if os.path.exists(database):
                os.remove(database)
            factory = ConnectionFactory()
            self.__conn = factory.get_connection()
            self.__cursor = factory.get_cursor()

            self.__cursor.execute("""
                CREATE TABLE IF NOT EXISTS PERSON (
                    ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    NAME VARCHAR(45) NOT NULL,
                    SALARY DECIMAL(12,2) NOT NULL
                );
            """)
            self.__conn.commit()

            self.__cursor.executemany(
                "INSERT INTO PERSON (NAME, SALARY) VALUES (?, ?)",
                people
            )
            self.__conn.commit()

        except Exception as err:
            print(f"Error: {err}")
            sys.exit()

    def insert(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass

    def get_by_id(self):
        pass

    def get_by_name(self):
        pass


c = Crud()