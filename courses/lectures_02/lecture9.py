# Lecture 09 

# Conceito sobre orientação a objetos - parte 02. 

#    1. Criar uma classe que exemplifique o uso de: 

#       •Atributos privados; 
#       •Métodos privados; 

#    2.  Criar um objeto da classe criada anteriormente e, após sua utilização, 
#       deletá-lo, demonstrando a tentativa de acesso a um item dessa classe 
#       após a deleção do objeto. 

#    3. Criar uma classe, por exemplo, Person (Pessoa), com atributos privados 
#       e implementar os métodos getter e setter utilizando o decorador 
#       @property. 

#    4.  Criar um método de classe utilizando @classmethod para a classe 
#       criada anteriormente e demonstrar sua utilização. 

class Person:
    cont = 0

    def __init__(self, *args, **kwargs):
        Person.___increment_count()
        self.__id = args[0]
        self.__name = kwargs["name"]
        print(self.__getstate__())

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        self.__name = value
    
    def ___increment_count():
        Person.cont+=1

    @classmethod
    def show_count(cls):
        print(f"contador: {cls.cont}")

    @staticmethod
    def show_count():
        print(f"Count: {Person.cont}")
    
    def __str__(self):
        return f"ID: {self.__id} | NAME: {self.__name}"
    
    def __enter__(self):
        return self
    
    def __exit__(self, v1, v2, v3):
        pass

with Person(1, name="Anderson") as obj:
    obj.name = "Anderson C."
    print(obj.name)
    print(obj.__str__())
    print(obj.__getstate__()) # dictionary
    obj.show_count()
    print(obj.__str__())

obj2 = Person(3, name="Fernanda") 
obj.show_count()

del obj2
try:
    print(obj2.__str__())
except NameError as err:
    print(f"Error: {err}")

Person.show_count()

i = 0
while i < 10:
    obj = Person(1, name="jhsjahdjas")
    print(Person.cont)
    obj.show_count()
    i+=1
    
print("\n\n\n\n\n")

# ------------------------------------------------------------------------------------

# Sobrecarga de Operadores 

#    5. Criar uma classe Vector com os atributos x e y. 

#    6.  Sobrecargar os operadores matemáticos para permitir, por exemplo, a 
#       soma dos atributos x e a soma dos atributos y de dois objetos Vector. 

#    7.  Sobrescrever o método __str__ para exibir o vetor de forma legível. 

class Vector:

    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def __str__(self):
        return f"X: {self.__x} | Y: {self.__y}"
    
    # sobrecargas de operadores:
    def __add__(self, other):
        return (self.__x + other.__x, self.__y + other.__y)
    
    def __sub__(self, other):
        return (self.__x - other.__x, self.__y - other.__y)


v1 = Vector(2,3)
v2 = Vector(4,5)
v3 = v1 + v2
print(v3)   

# ------------------------------------------------------------------------------------

#    8. Criar uma classe, por exemplo, Product (Produto), com os atributos 
#       name e price. 


#    9.  Sobrecargar o operador __gt__ para verificar se o preço de um objeto é 
#       maior ou menor que o preço de outro objeto. 

class Product:

    def __init__(self, prod, price):
        self.__prod = prod
        self.__price = price

    def __str__(self):
        return f"Product: {self.__prod} | Price: {self.__price}"
    
    def __gt__(self, other):
        return self.__price > other.__price
    
p1 = Product("Batata", 9.90)
p2 = Product("Chiclete", 3.00)
print(p1 > p2)
print(p1 < p2)

