# Lecture 03 

# Lista 

#    1. Criar um exemplo de uma lista com tipos diversos tipos de dados. 

import datetime
list = [123, "Anderson", 612365.11, False, 'M', datetime.date(1980,1,1), bytes("photoahsgdhasgd", "utf-8")]

#    2.  Criar um código que exemplifique a alteração de algum dado dessa lista 
#       mediante o seu índice. 

list[3] = True
print(list[3])

#    3. Criar um código que exemplifique a impressão de uma lista usando o 
#       print(). 

print(list)

#    4.  Criar um código que mostre o tamanho da lista de dados anteriormente 
#       criada. 

print(len(list))

#    5. Criar um código que tente ordenar a lista de dados diversos 
#       anteriormente criada com sort(). 

try:
    list.sort()
    print(list)
except TypeError as err:
    print("Erro ao ordernar lista com tipos diversos.")

#    6. Criar uma lista de números. 

nums = [6,5,7,4,8,3,9,2,0,1]

#    7. Criar um código que exemplifique a utilização dos métodos abaixo na 
#       lista de números anteriormente criada: 

#        •sort(), sort(reverse=True), reverse(), append(), insert(), remove(), 
#           pop(). 

copy_nums = nums.copy()
copy_nums.sort()
print(copy_nums)

copy_nums.sort(reverse=True)
print(copy_nums)

copy_nums.reverse()
print(copy_nums)

nums.append(4521524)
print(nums)

copy_nums = nums.copy()
copy_nums.insert(5, "x")
print(copy_nums)

nums.remove(4521524)
print(nums)

# Tupla 

#    1. Criar uma tupla de números. 

nums = (9,6,5,7,4,5,8,0,3,9,2,0,1)

try:
    nums[3] = 615261
    print(nums)
except TypeError as err:
    print("Erro ao alterar valor na tupla.")

#    2.  Criar um código para imprimir a tupla anteriormente criada. 

print(nums)

# 3. Criar um código para imprimir o type() da tupla criada. 

print(type(nums))

# 4.  Criar um código que exemplifique a impressão de um dado da tupla 
#    utilizando o seu índice. 

print(nums[3])

# 5. Criar um código que exemplifique a impressão de dados de uma tupla 
#    mediante um índice inicial e final de dados. 

print(nums[3:7])

# 6. Criar um código que exemplifique a execução das diversas funções 
#    referentes ao uso de tupla: 

#    •index(), count(), append(), sort(), sort(reverse=True), 
#    •e verificar se funcionam: 
#      reverse(), insert(), remove(), pop(). 

print(nums.index(8))
print(nums.count(0))

try:
    nums.append(52165261)
except AttributeError as err:
    print("Erro ao utilizar append() na tupla.")

try:
    nums.sort()
except AttributeError as err:
    print("Erro ao utilizar sort() na tupla.")

try:
    nums.insert(5, "x")
except AttributeError as err:
    print("Erro ao utilizar insert() na tupla.")

try:
    nums.remove(5)
except AttributeError as err:
    print("Erro ao utilizar remove() na tupla.")

try:
    nums.pop()
except AttributeError as err:
    print("Erro ao utilizar pop() na tupla.")

for el in nums:
    print(el)

# 7. Criar um código que exemplifique a utilização do if… else para  
#    verificar se uma string é um palíndromo, utilizando as letras da palavra 
#    "RADAR" (e outras palavras) em uma lista, com o uso das funções 
#    copy() e reverse(). 

palindromos = [['m','i','r','i','m'], ['c','a','f','é'], ['r','a','d','a','r'], ['c','o','i','s','a']]
for p in palindromos:
    p_temp = p.copy()
    p_temp.reverse()
    if p == p_temp:
        print(f"{"".join(p)} é um palíndromo!")
    else:
        print(f"{"".join(p)} não é um palíndromo.")

    