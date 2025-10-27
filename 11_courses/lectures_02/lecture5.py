# Lecture 05 

# Uso do looping em Python: While e For. 

# While 

#    1. Criar um código que exemplifique a execução de um looping simples. 

i = 0
while i < 10:
    print(i)
    i+=1

#    2.  Criar um código que exemplifique a execução de um looping infinito 
#       com break. 

i = 0
while True:
    if i == 1000:
        break
    i+=1
print("done!")

#    3. Criar uma lista de números. 

nums = [6,5,7,4,8,3,9,2,0,1]

#    4.  Criar um código que exemplifique a impressão de cada número 
#       mediante seu índice. 

i = 0
while i < len(nums):
    print(nums[i])
    i+=1

#    5. Criar uma lista de nomes de pessoas. 

people = ["Anderson", "Lexa", "Ava", "Sara", "Tiffany", "Jason", "Marc"]

#    6. Criar um código que exemplifique a impressão de cada nome mediante 
#       seu índice, nas seguintes formas: 

#       ●De forma ascendente; 
#       ●De forma descendente; 

i = 0
while i < len(people):
    print(people[i])
    i+=1

i = len(people)
while i > 0:
    print(people[i-1])
    i-=1

#    7. Criar uma tupla de números. 

nums = (6,5,7,4,8,3,9,2,0,1)

#    8. Criar um código que exemplifique a impressão de cada número pelo seu 
#       índice. 

i = 0
while i < len(nums):
    print(nums[i])
    i+=1

print(type(nums))

# For 

#    1. Criar uma tupla de números. 

nums = (6,5,7,4,8,3,9,2,0,1)

#    2.  Criar um código que exemplifique a impressão dos números da tupla 
#       anteriormente criada através do seu índice. 

for el in nums:
    print(el)

#    3. Criar uma tupla de nomes de pessoas. 

people = ("Anderson", "Lexa", "Ava", "Sara", "Tiffany", "Jason", "Marc")

#    4.  Criar um código que exemplifique a impressão de cada nome:

for el in people:
    print(el)

#    5. Criar uma string com um nome. 

name = "Anderson"

#    6. Criar um código que exemplifique que, mediante iteração sobre cada 
#       caractere, um caractere específico seja alterado utilizando um 
#       condicional. 

for c in name:
    if c == 'r':
        print('X', end="")
    print(c, end="")
print("\n")

#    7. Criar um código que exemplifique a criação de range(limite) de 
#       números e a iteração sobre esse mesmo range, fazendo o seguinte: 

#       •Apenas imprimindo; 
#       •Imprimindo mediante condição; 

for n in range(10):
    print(n)

print(type(range(10)))

for n in range(10):
    if n % 2 == 0:
        print(n)


# 8. Criar um código que exemplifique a criação de range(início, limite) de 
#    números e a iteração sobre esse mesmo range, fazendo o seguinte: 

#    •Apenas imprimindo; 
#    •Imprimindo mediante condição; 

for n in range(5,10):
    print(n)

print(type(range(5,10)))

for n in range(5,10):
    if n % 2 == 0:
        print(n)

# 9. Criar um código que exemplifique a criação de range(início, limite, 
#    passos) de números e a iteração sobre esse mesmo range, fazendo o 
#    seguinte: 

#    •Apenas imprimindo; 
#    •Imprimindo mediante condição; 

for n in range(1,10,3):
    print(n)

print(type(range(1,10,3)))

for n in range(1,10):
    if n % 2 != 0:
        print(n)


# 10.      Criar um range(início, limite, passos) e utilizar o WHILE para 
#    iterar sobre o mesmo fazendo o seguinte: 

#    •Apenas imprimindo; 
#    •Imprimindo mediante condição; 

nums = range(1,10,1)
while i < len(nums):
    if 10 / 2 == i:
        print(nums[i])
    i+=1
