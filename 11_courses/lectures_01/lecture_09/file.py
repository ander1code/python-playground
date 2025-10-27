class MyClass:
    def __init__(self, param1, param2):
        self.param1 = param1 # public
        self.__param2 = param2
        self.__private_method() # correto!
    
    def setParam2(self, param2):
        self.__param2  = param2

    def getParam2(self):
        return self.__param2
    
    def __private_method(self):
        print("Private Method!")

# -----------------------

try:
    obj = MyClass(123, "")
    print(obj.param1)
    del obj.param1 # deleting properties
    print(obj)
    del obj # deleting object
    print(obj.__str__) # error!
except NameError:
    print("Object deleted.")

# -----------------------

try:
    obj = MyClass(123, "Anderson")
    print(obj.param2) # error
except AttributeError:
    print("Error accessing private.")

# -----------------------

try:
    obj = MyClass(123, "Anderson")
    obj.setParam2("Anderson C.")
    print(obj.getParam2()) 
    obj.__private_method() # error
except AttributeError:
    print("Error accessing private.")

# -----------------------

class Person:
    def __init__(self, id, name):
        self.__id = id
        self.__name = name
    
    def get_id(self):
        return self.__id
    
    # def get_name(self):
    #     print(self.__name)
    #     return self.__name
    
    # def set_name(self, name):
    #     self.__name = name

    def set_name(self,name): # property nao funciona!!!
        self.__name = name
    
    @property
    def name(self):
        return self.__name

    def __str__(self):
        return f"ID: {self.__id} | NAME: {self.__name}"
    
class PhysicalPerson(Person):
    comment = "person"

    def __init__(self, id, name, birthday, gender):
        super().__init__(id, name) # constructor father
        self.__birthday = birthday
        self.__gender = gender
    
    def __str__(self):
                                             # property                   
        return f"ID: {self.get_id()} | NAME: {self.name} | BIRTHDAY: {self.__birthday} | GENDER: {self.__gender}"

    @classmethod
    def change_attribute(cls, comment):
        PhysicalPerson.comment = comment

pp = PhysicalPerson(123, "Anderson", "12/11/1981", "M")
pp.set_name("Anderson")
print(pp.name)
print(pp.__str__())

pp.change_attribute("person class!!!")
print(PhysicalPerson.comment)

# -----------------------

class A:
    def method(self):
        print("Class A!")

class B:
    def method(self):
        print("Class B!")

class C(A,B):
    def method(self):
        print("Class C!") # Esse será executado!

obj = C()
obj.method()

# -----------------------

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return (self.x + other.x, self.y + other.y) # X = 1 + 3 | Y = 2 + 4
    
    def __sub__(self, other):
        return (self.x - other.x, self.y - other.y) # X = 10 - 5 | Y = 8 - 4

    def __str__(self):
        return f"X:{self.x} | Y:{self.y}"
    
v1 = Vector(1,2)
print(f"Vetor 01 => {v1.__str__()}")
                
v2 = Vector(3,4)
print(f"Vetor 02 => {v2.__str__()}")

sum_vector = v1 + v2
print(f"Sum: {sum_vector.__str__()}")

# ---

v1 = Vector(10,8)
print(f"Vector 01 => {v1.__str__()}")
                
v2 = Vector(5,4)
print(f"Vector 02 => {v2.__str__()}")

sum_vector = v1 - v2
print(f"Sub: {sum_vector.__str__()}")


# -----------------------

class Product:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"NAME: {self.name} | PRICE: {self.price}"
    
    def __gt__(self, other):
        return self.price < other.price # inverti operador so de sacanagem :)
    

p1 = Product("Potator", 12.00)
p2 = Product("Beer", 9.00)

print(p1) # sem __str__()
print(p2) # sem __str__()

print(p1 > p2)
print(p2 > p1)
