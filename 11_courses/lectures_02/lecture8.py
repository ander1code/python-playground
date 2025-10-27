# Lecture 08 

# Conceito sobre orientação a objetos - parte 01. 

#    1. Criar uma classe, por exemplo, Person (Pessoa), que contenha o 
#       seguinte: 

#       •Atributo estático; 
#       •Construtores: sem parâmetros e com parâmetros; 
#       •Impressão do dado referente ao __getstate__ para esta classe; 
#       •Criação de um método estático usando o decorador @staticmethod; 
#       •Sobrescrição do método __str__ para fornecer uma representação 
#          legível do objeto; 

#       •Implementação da possibilidade de a classe ser utilizada dentro de 
#          uma declaração with. 


class Person:
    cont = 0

    def __init__(self, *args, **kwargs):
        Person.cont+=1
        self.id = args[0]
        self.name = kwargs["name"]
        print(self.__getstate__())
    
    @staticmethod
    def show_count():
        print(f"Count: {Person.cont}")

    def __str__(self):
        return f"ID: {self.id} | NAME: {self.name}"
    
    def __enter__(self):
        return self
    
    def __exit__(self, v1, v2, v3):
        pass

obj1 = Person(1, name="Jason")
obj2 = Person(2, name="Tiffany")
obj3 = Person(3, name="Ava")
obj4 = Person(4, name="Sara")
obj5 = Person(5, name="Anderson")
obj6 = Person(6, name="Emma")
Person.show_count()
print(obj5.__str__())
print(obj5.__getstate__()) # dictionary

with Person(7, name="Joana") as obj:
    print(obj.__str__())
    print(obj.__getstate__()) # dictionary

Person.show_count()