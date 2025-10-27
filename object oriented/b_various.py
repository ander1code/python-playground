
import datetime
import sys
import math

class Pessoa(object):
    
    #Constructor de uma classe:
    '''
    def __init__(self):
        self.codigo = 123
        self.nome = 'Anderson'
        self.dataNasc = datetime.date(1981,11,12)
        self.renda = 4500.00
    '''

    #def __init__(self, *args):
    #    self.codigo = args[0]
    #    self.nome = args[1]
    #    self.dataNasc = args[2]
    #    self.renda = args[3]
    #    self.carro = args[4]

    def __init__(self, **kwargs):
        self.codigo = kwargs['codigo']
        self.nome = kwargs['nome']
        self.dataNasc = kwargs['dataNasc']
        self.renda = kwargs['renda']
        self.carro = kwargs['carro']

    def Imprimir(self):
        print('\nDADOS CADASTRADOS: ')
        print('\nCódigo: %d' % (self.codigo))
        print('Nome: %s' % (self.nome))
        print('Data de Nascimento: %s' % (self.dataNasc))
        print('Renda: %.2f' % (self.renda))
        self.carro.Imprimir()
        
        print("\n\n\nImprimindo novamente...")
        print('\nDados sobre seu Carro: ')
        print('\nModelo: %s' % (self.carro.modelo))
        print('Ano: %d' % (self.carro.ano))
        print('Preço: %.2f' % (self.carro.preco))
        
        print('\n************************************************\n\n')


class Carro(object):
    
    def __init__(self, **kwargs):
        self.modelo = kwargs['modelo']
        self.ano = kwargs['ano']
        self.preco = kwargs['preco']

    def Imprimir(self):
        print('\nDados sobre seu Carro: ')
        print('\nModelo: %s' % (self.modelo))
        print('Ano: %d' % (self.ano))
        print('Preço: %.2f' % (self.preco))
        
#Criando objeto carro para ser atribuido.
carro = Carro(modelo="S10", ano=1998, preco=8000)

#Duas formas de Instanciar, por tupla ou dicionário:
#pessoa = Pessoa(123, 'Anderson', datetime.date(1981,11,12), 4500.00, carro)
pessoa = Pessoa(codigo=123, nome='Anderson', dataNasc=datetime.date(1981,11,12), renda=4500.00, carro=carro)

pessoa.Imprimir()

#Posso acessar diretamente o atributo nessa classe.
print("Nome: %s" % (pessoa.nome))

#Criando novo atributo.
pessoa.sobrenome = 'Conceição'
print("Sobrenome: %s" % (pessoa.sobrenome))

#Imprimindo o modelo do carro atribuido(Atribudo e um "atributo"):
print("Modelo: %s" % (pessoa.carro.modelo))

print("\n\n\n")

print('\n************************************************\n\n')

print("Dicionário e Classe:")

Cliente = {'nome' : 'Mara', 'dataNasc' : datetime.date(1959,6,8), 'renda' : 5000.50}
print(type(Cliente))
print(Cliente.__init__)

class Cliente(object):
    pass        

cli = Cliente()
cli.nome = 'Mara'
cli.dataNas = datetime.date(1959,6,8)
cli.renda = 5000.50
print(type(cli))
print(cli.__init__)

print('\n************************************************\n\n')



# -------------------

class MyClass(object):
    def greeting(self, name):
        print(f"Olá, {name}!")

def sum(n1, n2):
    return n1 + n2

"""
As primeiras linguagens de programação desenvolvidas nas décadas de 50 e 60 são reconhecidas como linguagens procedurais (ou orientadas a procedimentos).
"""

class Person:
    _cont = 0

    # def __init__(self, id, name):
    def __init__(self):
        self._id = None
        self._name = None
        print("Object created!")
        Person._cont += 1
    
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
    # def __init__(self, id, name, salary):
    def __init__(self):
        super().__init__()
        self.__salary = None
    
    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, salary):
        self.__salary = salary

    def __str__(self):
        return f"Object: {Person._cont} => ID: {self._id} | NAME: {self._name} | SALARY: {self._calc_salary(self.__salary)}"
    
    def _calc_salary(self, salary):
        return salary - ((salary * 10)/100)
    
p1 = NaturalPerson()
p1.id = 123; p1.name = "Anderson"; p1.salary = 1500.00;
print(p1)

p2 = NaturalPerson()
p2.id = 223; p2.name = "João"; p2.salary = 1800.00;
print(p2)

p3 = NaturalPerson()
p3.id = 111; p3.name = "Fernanda"; p3.salary = 2000.00;
print(p3)

# print(p1.__dict__)
# print(p1._NaturalPerson__salary)
# print(p1._name)

print(isinstance(p1, NaturalPerson))
print(issubclass(NaturalPerson, Person))


class Vector(object):
    "Vector class documentary."

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector((self.x + other.x),(self.y + other.y))
    
    def __eq__(self, other: object) -> bool:
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return f"X: {self.x} | Y: {self.y}"
    
v1 = Vector(2,3)
v2 = Vector(2,3)
print(v1 + v2)
print(v1 == v2)
    
print(id(v1), id(v2))
print(Vector.__doc__)

print(hasattr(v1, 'x'))
print(hasattr(v1, 'X'))

print(p1)
print(p1.__dict__)
delattr(p1, "_NaturalPerson__salary")

try:
    print(p1)
except AttributeError as err:
    print(f"Exception: {err}.")


print(p3)
del p3

try:
    print(p3)
except NameError as err:
    print("p3 foi excluído!")


class SingletonClass(object):
    __instance = None
    __count = 0

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            SingletonClass.__count += 1
        return cls.__instance

    def __str__(self):
        return f"Quantity: {SingletonClass.__count}"
    
for i in range(0,10):
    obj = SingletonClass()
    print(obj)


class MyClass(object):
    __counter = 0

    def __init__(self):
        pass

    # def __init__(self, parameter):
    #     self.parameter = parameter



    def method(self):
        print("object_method!")

    @classmethod
    def class_method_01(cls):
        cls.__counter += 1
        print("class_method_01!")

    def class_method(cls):
        cls.__counter += 1
        print("class_method_02!")
    
    class_method_02 = classmethod(class_method)

    @staticmethod
    def static_method():
        MyClass.__counter += 1
        print("static_method!")

    def show_counter(self):
        print(MyClass.__counter)

obj = MyClass()
MyClass.class_method_01()
MyClass.class_method_02()  
MyClass.static_method() 
obj.show_counter()

# refefinindo a classe Person e NaturalPerson:

class Thing:
    pass

class Person:
    _cont = 0

    # def __init__(self, id, name):
    def __init__(self):
        self._id = None
        self._name = None
        print("Object created!")
        Person._cont += 1
  
    def set_id(self, id):
        self._id = id

    def get_id(self):
        return self._id
    
    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name
    
    id = property(get_id, set_id, doc="ID property")
    name = property(get_name, set_name, doc="Name property.")

class NaturalPerson(Person, Thing):
    # def __init__(self, id, name, salary):
    def __init__(self):
        super().__init__()
        self.__salary = None
    
    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        self.__salary = salary

    salary = property(get_salary, set_salary, doc="Salary property")

    def __str__(self):
        return f"Object: {Person._cont} => ID: {self._id} | NAME: {self._name} | SALARY: {self._calc_salary(self.__salary)}"
    
    def _calc_salary(self, salary):
        return salary - ((salary * 10)/100)
    
p1 = NaturalPerson()
p1.id = 123; p1.name = "Anderson"; p1.salary = 1500.00;
print(p1)

p2 = NaturalPerson()
p2.id = 223; p2.name = "João"; p2.salary = 1800.00;
print(p2)

p3 = NaturalPerson()
p3.id = 111; p3.name = "Fernanda"; p3.salary = 2000.00;
print(p3)


class MyClass:

    def add(self, a, b):
        return a + b
        
    def add(self, a, b, c):
        return a + b + c
    
obj = MyClass()
try:
    print(obj.add(10,3))
except TypeError as err:
    print("add foi redefinido!")
print(obj.add(10,1,2))
        
# Overloading method

from multipledispatch import dispatch

class MyClass:

    @dispatch(int, int)
    def add(self, a, b):
        return a + b
        
    @dispatch(int, int, int)
    def add(self, a, b, c):
        return a + b + c
    
obj = MyClass()
print(obj.add(10,3))
print(obj.add(10,1,2))

# ----------------------------------

# Data Binding:

"""
Em Python, vinculação dinâmica é o processo de resolução de um método ou atributo em tempo de execução, em vez de em tempo de compilação.
"""

class shape(object):
    def draw(self):
        print("shape!")

class rectangle(shape):
    def draw(self):
        print("rectangle!")

class circle(shape):
    def draw(self):
        print("circle!")

class other_thing(shape):
    pass

shapes = [rectangle(), circle(), other_thing()]
for shp in shapes:
    shp.draw()

# ----------------------------------

# duck_function():
    
class shape(object):
    def draw(self):
        print("shape!")

class rectangle(shape):
    def draw(self):
        print("rectangle!")

class circle(shape):
    def draw(self):
        print("circle!")

class other_thing(shape):
    pass

def duck_function(obj):
    obj.draw()

shapes = [rectangle(), circle(), other_thing()]
for shp in shapes:
    duck_function(shp)
    
# ----------------------------------
    
message = "Hello, World!"
print(type(message), id(message))
message = 6125.11
print(type(message), id(message))

# ----------------------------------

# Classe Abstrata:

"""
Na terminologia de programação orientada a objetos, uma classe é considerada uma classe abstrata se não puder ser instanciada, ou seja, você pode ter um objeto de uma classe abstrata. No entanto, você pode usá-lo como classe base ou pai para construir outras classes.
"""

from abc import ABC, abstractmethod

class Person(ABC):

    def __init__(self):
        self.__id = None
        self.__name = None
    
    def _get_id(self):
        return self.__id
    
    def _set_id(self, id):
        self.__id = id

    # def _get_name(self):
    #     return self.__name
    
    # def _set_name(self, name):
    #     self.__name = name

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        self.__name = name

    id = property(_get_id, _set_id, "id property")
    # name = property(_get_name, _set_name, "name property")

class NaturalPerson(Person):

    def __init__(self, id, name, birthday):
        super().__init__()
        self.id = id
        self.name = name
        self.__birthday = birthday

    def __str__(self):
        return f"ID: {self.id} | NAME: {self.name} | BIRTHDAY: {self.__birthday}"

import datetime
p = NaturalPerson(123, "Anderson", datetime.date(1981,11,12))
print(p)

# ----------------------------------

class MyClass(object):
    def __init__(self):
        self.attr1 = None
        self._attr2 = "Hello, World!"
        self.__attr3 = True

obj = MyClass()
print(obj.attr1)
print(obj._attr2)

try:
    print(obj.__attr3)
except AttributeError as err:
    print(obj._MyClass__attr3)

print(obj.__dict__)
        
# ----------------------------------

from abc import ABC, abstractmethod

class my_interface(ABC):

    @abstractmethod
    def method_01(self):
        pass

    def method_02(self):
        pass

class implementation_class(my_interface):
    pass

try:
    obj = implementation_class()
except TypeError as err:
    print("method_01 not implemented!")

# ----------------------------------

class my_interface(ABC):

    def method_01(self):
        pass

    def method_02(self):
        pass

class implementation_class(my_interface):
    def method_01(self):
        print("method01!")

obj = implementation_class()
obj.method_01()

# ----------------------------------

# from .my_package.calculator import Calculator
from calculator_package.calculator import Calculator
obj = Calculator()
print(obj.flr(9,2))

# ----------------------------------

# Inner Class:

"""
A classe interna herda automaticamente os atributos da classe externa sem estabelecer formalmente a herança.
"""

class ExternalClass(object):

    def __init__(self,name):
        self.__sub = self.__InternalClass(name)

    def get_sub(self):
        return self.__sub
    
    sub = property(get_sub, None, "hgdashgdsh")

    class __InternalClass(object):

        def __init__(self,name):
            self.__sub = self.__InternalInternalClass(name)

        def get_sub(self):
            return self.__sub
        
        sub = property(get_sub, None, "hgdashgdsh")

        class __InternalInternalClass(object):

            def __init__(self, name):
                self.__name = name

            def greeting(self):
                print(f"Hello, {self.__name}!")

obj = ExternalClass("Anderson")
obj.sub.sub.greeting()


# anonymous class

calc_anonymous = type("", (object, ), {'x':None, 'y':None, 'sum': lambda self: self.x + self.y})
obj = calc_anonymous()
obj.x = 10
obj.y = 3
print(obj.sum())

# ----------------------------------

class SingletonClass(object):
    __count = 0
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super(SingletonClass, cls).__new__(cls)
            cls.__count+=1
        return cls.__instance

    def __init__(self):
        pass

    def get_count(self):
        return SingletonClass.__count

for i in range(0,10):
    obj = SingletonClass()
    print(id(obj), obj.get_count())


# wrapper_classes:
    
def my_decorator_class(object):
    class MyClass(object):

        def __init__(self, x, y):
            self.__x = x
            self.__y = y

        def method(self):
            print(f"{self.__x} + {self.__y} + {self.__x + self.__y}")

    return MyClass

class MyClass(object):

    def __init__(self, name):
        self.__name = name

    def method(self):
        print(f"Hello, {self.__name}!")

obj = MyClass("Anderson")
obj.method()

@my_decorator_class # "'reescrevo' a classe!"
class MyClass(object):

    def __init__(self, name):
        self.__name = name

    def method(self):
        print(f"Hello, {self.__name}!")

obj = MyClass(10,3)
obj.method()


# enum:

from enum import Enum

class subjects(Enum):
    ENGLISH = "E"
    MATHS = "M"
    GEOGRAPHY = "G"
    HISTORY = "H"

for s in subjects:
    print(s.name, s.value, type(s.value))


from enum import Enum

class person_data(Enum):
    ID = 123
    NAME = "Anderson"
    SALARY = 712632.11
    STATUS = True
    GENDER = 'M'
    BIRTHDAY = datetime.date(1981,11,12)
    STREET = {"address": "Rua da luz", "number": 123, "ditrict": "Gávea", "City": "Rio de Janeiro", "states": "RJ"}
    FUNCTIONS = ['Programmer', "Analyst", "DBA"]

for d in person_data:
    print(d.name, d.value, type(d.value))

# reflection
    
"""
Na programação orientada a objetos, reflexão refere-se à capacidade de extrair informações sobre qualquer objeto em uso.
"""

message = "Hello, World!"
    
def function():
    pass

class MyClass(object):
    pass

l = [1,2,3,4,5]

n = 521.11

obj = MyClass()

print(callable(message))
print(callable(function))
print(callable(MyClass))
print(callable(l))
print(callable(n))
print(callable(obj))


class MyClass(object):

    def __init__(self, name):
        self.name = name

    def method(self):
        print(f"Hello, {self.__name}!")

obj = MyClass("Anderson")
setattr(obj, "name", "Anderson C.")
print(getattr(obj, "name"))
print(hasattr(obj, "name"))
print(dir(obj))
print(isinstance(obj, MyClass))












