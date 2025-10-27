from math import *
from numbers import *
from sys import *

def Saudacao():
    for i in range(1,30):
        print("*", end="")
    print("\n\nSAUDAÇÃO:\n")
    print ("Hello, World!")

class Pessoa:
    pass

def TiparVariaveis():  
    for i in range(1,30):
        print("*", end="")
    
    print("\n\nTESTANDO FUNÇÕES DE TIPOS:\n")  
    #Converts x to an integer. base specifies the base if x is a string.
    print(int('35'))

    #Converts x to a floating-point number.
    print(float(35))
   
    #Creates a complex number.
    print(complex(-1.0, 0.0))
    
    #Converts object x to a string representation.
    print(str(35))
    
    #Converts object x to an expression string.
    nome = 35
    print(repr(nome))
    
    #Evaluates a string and returns an object.
    x = 30
    print(eval("x + 5"))
    
    #Converts s to a tuple.
    print(tuple("Anderson"))
    
    #Converts s to a list.
    print(list("Anderson"))
   
    #Converts s to a set.
    print(set("Anderson"))
    
    #Creates a dictionary. d must be a sequence of (key,value) tuples.
    print(dict(codigo = 123,  nome = "Anderson"))
    
    #Converts s to a frozen set.
    fset = frozenset("Anderson") #Conjunto "congelado"
    print(fset)

    #Converts a single character to its integer value.
    print(ord("A"))
    
    #Converts an integer to a hexadecimal string.
    print(hex(35))
    
    #Converts an integer to an octal string.
    print(oct(35))
 

def MathTeste():
    for i in range(1,30):
        print("*", end="")
    print("\n\nTESTANDO FUNÇÕES MATEMÁTICAS:\n")
    print(abs(35.511));
    print(ceil(35));
    print(exp(100));
    print(fabs(99.9));
    print(floor(99.9));
    print(log(10));
    print(log10(10));
    print(max(80,100,2000));
    print(min(80,100,2000));
    print(modf(35));
    print(pow(2,3));
    print(round(9.3));
    print(sqrt(3));
    print(pi)
    print(e)
    


Saudacao()
TiparVariaveis()
MathTeste()
