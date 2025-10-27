class BaseVector:
    pass


class Vector(BaseVector):
    """
    Classe Vector para teste.
    """
    __counter = 0

    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        Vector.__counter += 1

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @x.setter
    def x(self, x):
        self.__x = x

    @x.deleter
    def x(self):
        del self.__x

    @y.setter
    def y(self, y):
        self.__y = y

    def __str__(self):
        return f"Vector: [X:{self.__x}, Y:{self.__y}]"

    def __add__(self, other):
        return Vector(self.__x + other.x, self.__y + other.y)

    # @staticmethod
    # def get_counter():
    #     return Vector.__counter

    get_counter = staticmethod(__counter)

    @classmethod
    def class_method(cls, x, y):
        # Exemplo: cria um Vector padrão (0, 0)
        return cls(x, y)


# ------------
    
class Pessoa(object):
    
    def __init__(self, **kwargs):
        self.nome = kwargs['nome']
        self.renda = kwargs['renda']

    def Imprimir(self):
        print(self.nome)
        print(self.renda)
    
    def __le__(self, other):
        return self.renda <= other.renda

    def __eq__(self, other):
        return self.renda == other.renda

    def __ge__(self, other):
        return self.renda >= other.renda

    def __lt__(self, other):
        return self.renda < other.renda

    def __gt__(self, other):
        return self.renda > other.renda
    
    def __ne__(self, other):
        return self.renda != other.renda



p1 = Pessoa(nome='Anderson', renda=4500)
p2 = Pessoa(nome='Mara', renda=5000)

#Sobrecarga de operadores:
print(p1 <= p2)
print(p1 == p2)
print(p1 >= p2)
print(p1 < p2)
print(p1 > p2)
print(p1 != p2)
