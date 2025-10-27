class Person:
    """person class documentation."""

    __p_counter = 0
    
    def __init__(self, *args):

        if len(args) == 1:
            self.id = args[0]

        if len(args) == 2:
            self.id = args[0]
            self.name = args[1]
        
        Person.__p_counter += 1
        Person.__log("--- Criando objeto.")

    def __del__(self):
        print("---Object destroyed.")

    def __get_counter(cls):
        Person.__log("---Retornando quantidade de objetos criados.")
        return cls.__p_counter
    
    counter = classmethod(__get_counter)

    def __log(operation_name):
        print(f"{operation_name}")

    set_log = staticmethod(__log)

    def __repr__(self):
        result = f"Person ({self.id}" if hasattr(self, "id") else ""
        if hasattr(self, "name"):
            result += f", {self.name})"
        return result

    def __str__(self):
        result = f"ID: {self.id}" if hasattr(self, "id") else ""
        if hasattr(self, "name"):
            result += f",NAME: {self.name}"
        return result

print(f"\n- Name: {Person.__name__}\n")
print(f"- Dicitonary: {Person.__dict__}\n")
print(f"- Bases: {Person.__bases__}\n")
print(f"- Module: {Person.__module__}\n")

Person.set_log("--- Criando de erro ao executar algo com objeto destruído.")
obj = Person()

Person.set_log("--- Deletando objeto.")
del obj

try:
    Person.set_log("--- Verificado se name existe.")
    print(f"hasattr: {hasattr(obj, "name")}")
    
except NameError as err:
    Person.set_log("--- Mensagem de erro ao executar algo com objeto destruído.")
    print(f"Error: {err}")



obj = Person(1)

print(f"hasattr: {hasattr(obj, "name")}")
print(f"hasattr: {setattr(obj, "name", "Anderson")}")

print(obj)

if hasattr(obj, "name"):
    print(getattr(obj, "name"))

delattr(obj, "name")

if not hasattr(obj, "name"):
    print("Name no exists!")

          

print(type(obj))

obj2 = Person(123, "Joana")

print(obj2.__dict__)

print(Person.counter())

print(obj2.__dict__)
print(str(obj2))
print(repr(obj2))

test = {1,2,3}
print(type(test))

test = [1,2,3]
print(type(test))

test = (1,2,3)
print(type(test))

test = 1,2,3
print(type(test))

test = "1,2,3"
print(type(test))

# ------------------------------------------------------------

import re
from asyncio.windows_events import NULL
from email.mime import base

class Person:
    'Documentação da classe People.'
    cont = 0

    def __init__(self, id, name):
        self.id = id
        self.name = name
        Person.cont += 1

    def __del__(self):
        print("Objeto destruído.")


class PhysicalPerson(Person):
    def __init__(self, id, name, cpf):
        self.id = id
        self.name = name
        self.cpf = cpf

    def __del__(self):
        print("PhysicalPerson destruído")

    def __str__(self):
        return ("ID: %d | Name: %s | CPF: %s " % (self.id, self.name, self.cpf))


for i in range(0, 10):
    p = Person(1, "Anderson")

print("Quantidade: %d" % (Person.cont))

p1 = Person(1, "Anderson")
print("ID: %d | Name: %s" % (p1.id, p1.name))
print("ID: %d | Name: %s" % (getattr(p1, "id"), getattr(p1, "name")))

setattr(p1, "name", "Anderson C.")
print("ID: %d | Name: %s" % (getattr(p1, "id"), getattr(p1, "name")))

delattr(p1, "id")

try:
    print("ID: %d | Name: %s" % (getattr(p1, "id"), getattr(p1, "name")))
except:
    print("ID não mais definido.")

# informações sobre a classe:

print(Person.__doc__)
print(Person.__name__)
print(Person.__module__)
print(Person.__bases__)
print(Person.__dict__)

# Não usa o objeto?

print("Tem salario? %s" % hasattr(p1, "salary"))

del Person

# NameError: name 'Person' is not defined
# print("Quantidade: %d" %(Person.cont))

pp = PhysicalPerson(123, "Anderson", "42376543211")
print(pp.__str__())


class Classe:
    __privateAttr = "Atributo oculto"
    __contador = 0

    def __init__(self, num):
        self.num = num
        self.__contador += 1

    def __add__(self, other):
        return Classe(self.num + other.num)

    def getCount(self):
        print(self.__contador)


c1 = Classe(10)
c2 = Classe(30)
print((c1 + c2).num)
print(c1.getCount())

# AttributeError: 'Classe' object has no attribute '__privateAttr'
# print(c1.__privateAttr)


def regex():
    email = "abdhdhasg@hsjhdjshds.com"
    pattner = "/(^$|^.*@.*\..*$)/"
    result = re.match(pattner, email, re.U | re.IGNORECASE)
    print("retorno: %s" % (result))


regex()


