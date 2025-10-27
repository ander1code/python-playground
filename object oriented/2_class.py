class Person:
    __counter = 0

    def __init__(self, *args):
        if len(args) == 2:
            self._id = args[0]
            self._name = args[1]
       
        # Se _id existir, define property id na classe (se ainda não estiver definida)
        if hasattr(self, "_id"):
            def set_id(inst, id_):
                inst._id = id_
            def get_id(inst):
                return inst._id
            if not hasattr(self.__class__, "id"):
                self.__class__.id = property(get_id, set_id, doc="id")
        
        # Se _name existir, define property name na classe (se ainda não estiver definida)
        if hasattr(self, "_name"):
            def set_name(inst, name):
                inst._name = name
            def get_name(inst):
                return inst._name
            if not hasattr(self.__class__, "name"):
                self.__class__.name = property(get_name, set_name, doc="name")
            
        Person.__counter += 1

    def get_counter():
        return Person.__counter


class NaturalPerson(Person):

    def __init__(self, *args):
        super().__init__(*args)
        if len(args) == 3:
            self.__birthday = args[2]
        else:
            # Para evitar ausência do atributo, define um valor padrão
            self.__birthday = None
            
        if hasattr(self, "_NaturalPerson__birthday"):
            def set_birthday(inst, birthday):
                inst.__birthday = birthday
            def get_birthday(inst):
                return inst.__birthday
            if not hasattr(self.__class__, "birthday"):
                self.__class__.birthday = property(get_birthday, set_birthday, doc="birthday")

    def __str__(self):
        print(self.__doc__)  # Imprime a docstring, se houver
        s = ""
        if hasattr(self, "_id"):
            s += "ID: {}".format(self._id)
        if hasattr(self, "_name"):
            s += "| NAME: {}".format(self._name)
        if hasattr(self, "_NaturalPerson__birthday"):
            s += "| BIRTHDAY: {}".format(self.__birthday)
        return s


# Testando o código
import datetime

p1 = NaturalPerson()
print(p1)  # p1 sem parâmetros; não possuirá id, name ou birthday

p2 = NaturalPerson(1, "Anderson")
print(p2)  # Exibe ID e NAME, mas birthday ficará como None

p3 = NaturalPerson(1, "Anderson", datetime.date(1981, 1, 1))
print(p3)  # Exibe ID, NAME e BIRTHDAY

try:
    print(p3._name)  # _name foi definido pelo construtor, assim não gera erro
except AttributeError as err:
    print(err)

try:
    print(p3.__birthday)  # Gera AttributeError, pois __birthday sofre name mangling
except AttributeError as err:
    print(err)

print(Person.get_counter())

# Acessando o atributo __birthday via name mangling (não recomendado, mas para demonstração)
print(p3._NaturalPerson__birthday)

# Acessando via properties definidas na classe
print(f"{p3.id}, {p3.name}, {p3.birthday}")
