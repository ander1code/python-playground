class Person:
    name = "Anderson"

print(f"Name: {Person().name}")

# ------------ 

class Person:
     # statics
    comment = "Person class!"
    name = "Anderson"

    # def __init__(self): # empty constructor
    #     pass

    def __init__(self, name):
        self.name = name

    def get_class_datas(self):
        print(f": {self.__getstate__}")
    
    def __str__(self):
        return f"Name: {self.name}"

    @staticmethod
    def static_method():
        print("Static methods.")
    
person = Person("Anderson C.")
print(person.__str__())
print(person.comment)

# self => current instance.

person = Person("Fernanda")
person = Person("Lucia")
person = Person("Renata")
person = Person("Sara")
person = Person("Daphne")
# print(f"Count: {Person.i}")

Person.static_method()

# ------------ 
