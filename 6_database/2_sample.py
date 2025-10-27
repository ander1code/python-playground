class Person:
    'Documentação da classe People.'
    cont = 0

    def __init__(self, id, name):
        self.id = id
        self.name = name
        Person.cont += 1

    def __del__(self):
        print("Objeto destruído.")

class DatabaseTest:
    __conn = ""
    __cursor = ""

    def __init__(self):
        import MySQLdb
        try:
            self.conn = MySQLdb.connect("localhost", "root", "password", "dbPython", 3306)
            self.cursor = self.conn.cursor()
            print('Conectado!')
        except Exception as ex:
            print(ex)
    
    def Inserir(self, person):
        try:
            self.cursor.execute(
                "INSERT INTO PERSON VALUES(%d, '%s')" % (person.id, person.name))
            self.conn.commit()
            return 1
        except:
            self.conn.rollback()
            return -1
        finally:
            self.conn.close()

    def Editar(self, person):
        try:
            self.cursor.execute(
                "UPDATE PERSON SET name = '%s' WHERE id = %d" % (person.name, person.id))
            self.conn.commit()
            return 1
        except:
            self.conn.rollback()
            return -1
        finally:
            self.conn.close()


    def Buscar(self):
        try:
            people = self.cursor.execute("SELECT * FROM PERSON")
            return people
        except Exception as ex:
            return -1
        finally:
            self.conn.close()

    def Deletar(self, person):
        try:
            self.cursor.execute(
                "DELETE FROM PERSON WHERE id = %d" % (person.id))
            self.conn.commit()
            return 1
        except:
            self.conn.rollback()
            return -1
        finally:
            self.conn.close()


    def __del__(self):
        return


obj = DatabaseTest()
p = Person(1, "Anderson")
# print(obj.Inserir(p))
# p = Person(1, "Anderson C.")
# print(obj.Editar(p))
# print(obj.Deletar(p))

people = obj.Buscar()
print("gashdasgdjhs" + people)



