# Lecture 01 

#    1. Criar um código que exemplifique a impressão de uma mensagem 
#       simples na tela. 

print("Hello, World!")

#    2.  Criar um código que exemplifique a impressão do type() para variáveis 
#       de diversos tipos. 

from datetime import date
v1, v2, v3, v4, v5, v6 = 123, "Anderson", 7721.11, 'M', date(1981,11,12), True
print(f"{type(v1)} | {type(v2)} | {type(v3)} | {type(v4)} | {type(v5)} | {type(v6)}")

#    3. Criar um código que exemplifique o uso dos diversos tipos de aspas do 
#       Python em strings. 

str1 = 'string 01'
str2 = "string 02"
str3 = """string 03"""
print(f"{str1} | {str2} | {str3}")

#    4.  Criar um código que exemplifique a criação de função das seguintes 
#       maneiras: 

#       1. Sem parâmetros; 

def function_01():
    pass

#       2. Com parâmetros; 

def function_02(arg):
    pass

#       3. Com retorno; 

def function_03():
    return

#    5. Criar um código que exemplifique a utilização de operadores 
#       matemáticos: +=, *=, -= … 

num = 1
num += 3
print(num)
num -= 1
print(num)
num *= 4
print(num)
num /= 2
print(num)
num %= 2
print(num is 0.0)

#    6. Criar um código que exemplifique a utilização de operadores lógicos e 
#       dos valores True e False, diretamente no print(). 

print(True and False)
print(False or False)
print(True and (False or True))
print(False and (False or False))
print(not (False or False))

opc = True
if opc is not False:
    print("True!")

#    7. Criar um código que exemplifique a conversão de tipo de uma variável 
#       e a impressão do type() dessa variável. 

name = "Anderson"
print(type(name))
num_str = "6531.11"
num_flt = float(num_str)
print(type(num_flt))
num_str = "1"
num_flt = int(num_str)
print(type(num_flt))
num_str = "1"
num_flt = bytes(num_str, "utf-8")
print(type(num_flt))
num_str = "True"
num_flt = bool(num_str)
print(type(num_flt))
birthday = date(1981,1,1)
print(type(birthday))
print(type(list()))
print(type(dict()))
from collections import *
nt = namedtuple("Course", ["language","hasjhdjashj"])
print(type(nt))
print(type(Counter()))
print(type(defaultdict()))
print(type(ChainMap()))

#    8. Criar um código que exemplifique a entrada de dados para uma 
#       variável, nas seguintes formas: 

#       •Entrada simples de dados; 

num = input("Enter number: ")
print(num)

#       •Conversão de tipo na entrada dos dados; 

try:
    num = input("Enter number: ")
    print(int(num))

    num = int(input("Enter number: "))
    print(num)
except ValueError as err:
    print(f"Erro: {err}")
    
