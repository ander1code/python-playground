def f8(id=123, name='Anderson'):
    print('ID: %d | Name: %s' %(id, name))
    pass


from datetime import date

# Positional and Named Arguments :

# Positional Arguments:

def show_data_pos(*args):
    print(f"args: {args}")
    print(f"Name: {args[1]}")
    for data in args:
        print(data)
    print(f"Type: {type(args)}")

show_data_pos(1, "Anderson", date(1981,1,1), 712632.11, True)

print("-----------------------------------------------------------")

# Named Arguments:

def show_data_nom(**kwargs):
    print(f"{kwargs}")
    print(f"Name: {kwargs["name"]}")
    for k, v in kwargs.items():
        print(f"{k.capitalize()}: {v}")
    print(f"{type(kwargs)}")

# show_data_nom(1, "Anderson", date(1981,11,12), 712632.11, True) # error

show_data_nom(id=1, name="Anderson", birthday=date(1981,1,1), salary=712632.11, status=True)


# --------------

# Argumentos 

# Argumentos Posicionais: 

#    1. Crie um código que exemplifique uma função que receba parâmetros 
#       posicionais e, dentro dessa função, execute um print(type()) para 
#       exibir o tipo dos argumentos passados. 

def show_types_by_arg_pos(*args):
    for a in args:
        print(a)

from datetime import date
show_types_by_arg_pos(123, "Anderson", 'M', 82173.11, date(1981,1,1), bytes("jhsjahdjashdjs", 'utf-8'))

#    2.  Crie uma classe cujo construtor (sobrescrito) receba atributos 
#       posicionais. 

class Person:

    def __init__(self, *args):
        self.__id = args[0]
        self.__name = args[1]

    def __str__(self):
        return f"ID: {self.__id} | NAME: {self.__name}"

p = Person(123, "Anderson")
print(p)

# Argumentos Nominais: 

#    1. Crie um código que exemplifique uma função que receba parâmetros 
#       nominais e, dentro dessa função, execute um print (type())para 
#       exibir o tipo dos argumentos passados. 

def show_types_by_arg_name(**kwargs):
    print(kwargs["name"])
    for k,v in kwargs.items():
        print(f"{k.capitalize()}: {v}")

from datetime import date
show_types_by_arg_name(id=123, name="Anderson", gender='M', salary=82173.11, birthday=date(1981,1,1), picture=bytes("jhsjahdjashdjs", 'utf-8'))

#    2.  Crie uma classe cujo construtor (sobrescrito) receba atributos nominais. 

class Person:

    def __init__(self, **kwargs):
        self.__id = kwargs["id"]
        self.__name = kwargs["name"]

    def __str__(self):
        return f"ID: {self.__id} | NAME: {self.__name}"

p = Person(id=123, name="Anderson")
print(p)

# Geral: 

#    1. Crie uma classe cujo construtor (sobrescrito) receba atributos 
#       posicionais e nominais. 


class Person:

    def __init__(self, *args, **kwargs):
        self.__id = args[0]
        self.__name = kwargs["name"]
        self.__birthday = kwargs["birthday"]

    def __str__(self):
        return f"ID: {self.__id} | NAME: {self.__name} | BIRTHDAY: {self.__birthday}"

from datetime import date
p = Person(123, name="Anderson", birthday=date(1981,1,1))
print(p)
