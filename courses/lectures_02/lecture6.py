# Lecture 06 

# Uso de funções. 

#    1. Criar um código que exemplifique a criação de uma função com uma 
#       mensagem de saudação, fazendo o seguinte: 

#       •Impressão simples; 

def greeting():
    print("Hello, World!")

greeting()

#       •Impressão utilizando o end=; 

def greeting():
    print("Hello,","",end="World!")

greeting()

#    2.  Criar um código que exemplifique a criação de uma função com valor 
#       pré-definido e mensagem de saudação, fazendo o seguinte: 

#       •Impressão simples; 

def greeting(name="Anderson"):
    print(f"\nHello, {name}!")

greeting()

#       •Impressão utilizando o end=; 

def greeting(name="Anderson"):
    print(f"Hello, ", end=name + "!")
greeting()

#    3. Criar um código que exemplifique uma função que mostre o tamanho 
#       de uma coleção a ser passada. 
print("\n")
def show_len_collection(col):
    print(len(col))

list = [6,5,7,4,8,3,9,2,0,1]
set = {6,7,4,8,3,0,1}
tuple =  (6,5,3,9,2,0)
dict = {
        "key1": "value1", 
        "key2": "value2", 
        "key3": "value3", 
        "key4": "value4", 
        "key5": "value5", 
       }

show_len_collection(list)
show_len_collection(set)
show_len_collection(tuple)
show_len_collection(dict)

#    4.  Criar um código que exemplifique uma função que receba uma coleção 
#       e imprima seus itens separados por vírgula. 

def show_itens(col):
    print(f"\ncollection type: {type(col)}")
    for i in col:
        print(i, end=", ")

show_itens(list)
show_itens(set)
show_itens(tuple)
show_itens(dict)


# 5. Criar um código que exemplifique uma função que realize recursão (ou 
#    seja, que chame a si mesma). 

# recursão descendente:

print("\n")
def recursion_descendent(n):
    if n == 0:
        return
    print(n)
    recursion_descendent(n-1)

recursion_descendent(10)

# recursão ascendente:

print("\n")
def recursion_ascendent(n=0,limit=10):
    if n == limit:
        return
    print(n)
    recursion_ascendent(n=n+1)

recursion_ascendent()


# 6. Criar um código que exemplifique uma função que realize o cálculo de 
#    um "fatorial" entre dois números (início e fim) no formato de soma. 

def calc_factorial_sum(n):
    if((n==0)or(n==1)):
        return 1
    return calc_factorial_sum(n-1)+n
print(calc_factorial_sum(5))

# 7. Criar um código que exemplifique uma função que realize o cálculo de 
#    um "fatorial" entre dois números (início e fim) no formato de 
#    multiplicação. 

def calc_factorial_mlt(n):
    if((n==0)or(n==1)):
        return 1
    return calc_factorial_mlt(n-1)*n
print(calc_factorial_mlt(5))

# 8. Criar um código que exemplifique uma função que receba um valor em 
#    dólar e o converta para real. 

def convert_dollar_to_real(dollar):
    print(dollar * 5.87)
convert_dollar_to_real(2.50)

# 9. Crie uma lista de nomes de pessoas. 

people = ["Anderson", "Fernanda", "Renata", "Andreia", "Marcella", "Cris", "Juliana"]

# 10.      Criar um código que exemplifique uma função que imprima esses 
#    nomes utilizando o conceito de recursão. 

def print_list(param, index=0):
    if(len(param) == index):
        return
    print(param[index])
    print_list(param, index+1)
print_list(people)