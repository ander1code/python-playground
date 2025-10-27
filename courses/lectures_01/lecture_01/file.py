print("Hello, Brazil!", "Hello, World!")
print(43)

num1 = 20
num2 = 23
soma = num1 + num2
print(soma)

# Comentario sobre o codigo.

name = "Anderson"
print("Hello,", name + "!")

# Get variable type

price = 43.11
print(type(price))
price = True
print(type(price))
price = "Anderson"
print(type(price))
price = 'A'  # é string!
print(type(price))
price = 123
print(type(price))
price = None
print(type(price))

# Aspas

name = "Anderson"
print(name, type(name))
name = 'Anderson'
print(name, type(name))
name = '''Anderson'''
print(name, type(name))

# Function

def greeting(name="Anderson"):
    print("Hello, " + name + "!")

def sum(num1, num2):
    return num1 + num2

greeting("Fulana")

print(sum(40, 30))

"""
Uso de 
comentarios 
em python
"""
num = 10
num += 10
print(num)

num %= 20
print(num)

print(not True)
print(False and False)
print(False or True)

a,b = 1,2
print(a + b)

# type conversion:
num = int("43")
print(type(num))

# read

name = input("Enter your name: ")
print(greeting(name))


# read generic:

value = input("Enter: ")
print(type(value))

# read generic:

def sum(num1, num2):
    print(num1 + num2)

num1 = input("Enter num1: ")
num2 = input("Enter num2: ")
sum(int(num1), int(num2))

# -------

num1 = float(input("Enter num1: "))
num2 = float(input("Enter num2: "))
sum(num1, num2)

