# Python - Abstract Base Classes

from abc import ABC, abstractmethod

class BaseClass(ABC):
    @abstractmethod
    def method01(self):
        pass

    @abstractmethod
    def method02(self):
        pass

    def method03(self):
        print("No abstract method.")

class ChildClass(BaseClass):
    def method01(self, name):
        print(f"Hello, {name}!")

    def method02():
        pass

obj = ChildClass()
obj.method01("Anderson")
obj.method03()

# ---------

from abc import *

class Pessoa(metaclass=ABCMeta):
    
    @abstractmethod
    def setCodigo(self, codigo):
        raise NotImplementedError("setCodigo não foi implementado.")

    @abstractmethod
    def getCodigo(self):
        raise NotImplementedError("getCodigo não foi implementado.")

    @abstractmethod
    def setNome(self, nome):
        raise NotImplementedError("setNome não foi implementado.")

    @abstractmethod
    def getNome(self):
        raise NotImplementedError("getNome não foi implementado.")

    @abstractmethod
    def setEmail(self, email):
        raise NotImplementedError("setEmail não foi implementado.")

    @abstractmethod
    def getEmail(self):
        raise NotImplementedError("getEmail não foi implementado.")
   

class PessoaFisica(Pessoa):

    contador = 0

    def __init__(self, **kwargs):
        if len(kwargs) == 3:
            self.__codigo = kwargs['codigo']
            self.__nome = kwargs['nome']
            self.__email = kwargs['email']
        else:
            self.__codigo = 0
            self.__nome = ''
            self.__email = ''
        PessoaFisica.contador += 1
    
    def setCodigo(self, codigo):
        self.__codigo = codigo

    def getCodigo(self):
         return self.__codigo

    def setNome(self, nome):
        self.__nome = nome

    def getNome(self):
        return self.__nome

    def setEmail(self, email):
        self.__email = email

    def getEmail(self):
        return self.__email

    def PrintContador(self):
        print(PessoaFisica.contador) 

    def __str__(self):
        return ("%d -- %s -- %s" %(self.__codigo, self.__nome, self.__email))

    def __del__(self):
        print("Objeto Pessoa Fisica foi destruido.")

    def __doc__(self):
        print("Classe Pessoa Física.")




pf = PessoaFisica(codigo=123, nome="Anderson", email="anderson@yyy.xxx")
del(pf)
pf = PessoaFisica(codigo=123, nome="Anderson", email="anderson@yyy.xxx")
del(pf)
pf = PessoaFisica(codigo=123, nome="Anderson", email="anderson@yyy.xxx")
del(pf)
pf = PessoaFisica(codigo=123, nome="Anderson", email="anderson@yyy.xxx")
del(pf)
pf = PessoaFisica(codigo=123, nome="Anderson", email="anderson@yyy.xxx")
del(pf)
pf = PessoaFisica(codigo=123, nome="Anderson", email="anderson@yyy.xxx")
del(pf)
pf = PessoaFisica(codigo=123, nome="Anderson", email="anderson@yyy.xxx")
pf.PrintContador()
del(pf)


#Informações sobre classes:
print ("PessoaFisica.__doc__:", PessoaFisica.__doc__)
print ("PessoaFisica.__name__:", PessoaFisica.__name__)
print ("PessoaFisica.__module__:", PessoaFisica.__module__)
print ("PessoaFisica.__bases__:", PessoaFisica.__bases__)
print ("PessoaFisica.__dict__:", PessoaFisica.__dict__)



#Verificando relacionamentos de classes:
print (issubclass(PessoaFisica,Pessoa))

pf = PessoaFisica(codigo=123, nome="Anderson", email="anderson@yyy.xxx")
print (isinstance(pf, PessoaFisica))
del(pf)







