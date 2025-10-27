
#Guardada em C:/python/lib
class Calculadora(object):
    def __init__(self, **kwargs):
        self.__valor1 = kwargs['valor1']
        self.__valor2 = kwargs['valor2']

    def Somar(self):
        return self.__valor1+self.__valor2

    def Subtrair(self):
        return self.__valor1-self.__valor2

    def Multiplicar(self):
        return self.__valor1*self.__valor2

    def Dividir(self):
        return self.__valor1/self.__valor2
    
    def Modular(self):
        return self.__valor1%self.__valor2