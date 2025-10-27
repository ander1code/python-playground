# Lambda 

#     1.Crie um código que exemplifique o uso de lambda para realizar 
#       operações matemáticas, como somar, subtrair, multiplicar, dividir, 
#       aplicar o módulo e calcular a potência. 

sum = lambda x, y: x + y
sub = lambda x, y: x - y
mlt = lambda x, y: x * y
div = lambda x, y: x / y
mod = lambda x, y: x % y
sqr = lambda x, y: x**y

print(sum(1,2))
print(sub(1,2))
print(mlt(1,2))
print(div(1,2))
print(mod(1,2))
print(sqr(1,2))

#    2. Crie um código que exemplifique o seguinte: utilizando um loop for 
#       com range(início, fim, passos), cada número deve ser captado e 
#       multiplicado por um valor informado, usando lambda. Em seguida, 
#       exiba os resultados de duas maneiras: 

#          •Impressão simples; 

for num in map(lambda x: x * 5, range(11)):
    print(num)

#          •Valores separados por vírgula. 

for num in map(lambda x: x * 5, range(11)):
    print(num, end=", ")

#    3.Crie uma lista contendo palavras em diferentes formatos: todas em 
#       minúsculas, todas em maiúsculas e com o primeiro caractere em 
#       maiúsculas. 

words = ["HDASJDHASJ","jashdjashdjas","WhjsdhAjhsjdhs", "Wjhdasjdhsjd","YUYEUYREUEY"]

#    4. Crie um código que use lambda para converter as palavras da lista 
#       criada no item anterior para: 

#          •Maiúsculas (utilizando upper()); 

for w in map(lambda w: w.upper(), words):
    print(w)

#          •Minúsculas (utilizando  lower()); 

for w in map(lambda w: w.lower(), words):
    print(w)

#          •Com o primeiro caractere em maiúsculas (utilizando 
#            capitalize()). 

for w in map(lambda w: w.capitalize(), words):
    print(w)

#    5.Crie um código que exemplifique o seguinte: utilizando lambda, 
#       converta os caracteres para maiúsculas, minúsculas e com o primeiro 
#       caractere em maiúsculas; em seguida, ordene corretamente os 
#       resultados. Toda essa operação deve ser executada dentro de um único 
#       print(). 

print(sorted(list(map(lambda w: w.upper(), words))))
print(sorted(list(map(lambda w: w.lower(), words))))
print(sorted(list(map(lambda w: w.capitalize(), words))))

#    6.Crie uma lista de nomes de pessoas. 

people = ["Anderson", "Renata", "Fernanda", "Carla", "Jason"]

#    7.Crie um código que ordene a lista de nomes criada anteriormente 
#   utilizando lambda e, em seguida, itere sobre os dados exibindo-os. 


# NAO LEMBRO


# 8.Crie uma lista de números desordenados. 

nums = [6,5,7,4,8,3,9,2,0,1]

# 9.Crie um código que exemplifique o seguinte: selecione um número da 
#   lista criada anteriormente e multiplique-o por um valor informado, 
#   utilizando lambda. Em seguida, exiba a nova lista resultante com um 
#   print(). 



# 10.     Crie um código que, dada uma lista de números, verifique se cada 
#   número é par utilizando lambda. Crie duas versões deste exercício, uma 
#   utilizando map() e outra com filter(). 

nums.sort()

print("\n")

for n in map(lambda x: x % 2 == 0, nums):
    print(n, end=", ")
    
print("\n")

for n in filter(lambda x: x % 2 == 0, nums):
    print(n, end=", ")

print("\n")

for n in map(lambda x: x % 2 == 1, nums):
    print(n, end=", ")

print("\n")

for n in filter(lambda x: x % 2 == 1, nums):
    print(n, end=", ")

print("\n")


# 11.     Crie um código que exemplifique o cálculo do somatório de todos 
#   os números da lista criada, utilizando reduce()com lambda. 

from functools import reduce
print(reduce(lambda x, y: x + y, nums))

# 12.     Crie um código que exemplifique a multiplicação de todos os 
#   números da lista, utilizando reduce()com lambda. 

nums.remove(0)
print(reduce(lambda x, y: x * y, nums))

# 13.     Crie um código que demonstre o uso das funções min() e max(), 
#   comparando dois números. 

print(min(nums))

# 14.     Crie um código que, utilizando lambda, busque o maior valor da 
#   lista de números criada anteriormente. 

print(max(nums))

# 15.     Crie uma classe que representará uma calculadora, implementando 
#   as operações matemáticas por meio de funções lambda. 

class CalcLambda:

    def sum(self, x, y):
        f =  lambda x, y: x + y
        return f(x, y)

    def sub(self, x, y):
        f =  lambda x, y: x - y
        return f(x, y)

    def mlt(self, x, y):
        f =  lambda x, y: x * y
        return f(x, y)

    def div(self, x, y):
        f =  lambda x, y: x / y
        return f(x, y)

    def mod(self, x, y):
        f =  lambda x, y: x % y
        return f(x, y)

    def sqr(self, x, y):
        f =  lambda x, y: x ** y
        return f(x, y)

    def __enter__(self):
        return self
    
    def __exit__(self, v1, v2, v3):
        pass

with CalcLambda() as obj:
    print(obj.sum(3,4))
    print(obj.sub(3,4))
    print(obj.mlt(3,4))
    print(obj.div(3,4))
    print(obj.mod(3,4))
    print(obj.sqr(3,4))
    

# 16.     Crie uma lista contendo sublistas de números, que representem, 
#   por exemplo, o placar de 3 sets. 

sets = [[1,2,3],[4,5,6],[7,8,9]]


# 17.     Crie um código que realize uma operação matemática com os 
#   números das listas internas, considerando o mesmo índice para cada 
#   sublista (por exemplo:  [lista1[1] + lista2[1] + lista3[1]]). 




# 18.     Crie um dicionário contendo id e nome de pessoas. 





# 19.     Crie um código que exiba os dados de  idrelacionados aos nomes 
#   das pessoas. 

# 20.     Crie um código que imprima os nomes das pessoas do dicionário 
#   criado, obedecendo a um critério específico, como, por exemplo, que o 
#   primeiro caractere do nome seja igual a um caractere informado. 

# 21.     Crie um código que exiba os nomes das pessoas do dicionário 
#   criado, considerando apenas os  ids que sejam números pares. 

# 22.     Crie duas listas de números. 

# 23.     Crie um código que multiplique os itens das duas listas criadas 
#   anteriormente, levando em consideração o índice correspondente (por 
#   exemplo,  list1[1] * list2[1],  list1[2] * list2[2], etc.). 

# 24.     Utilize reduce()para determinar qual é o maior número presente 
#   em uma lista. 

# 25.     Execute uma operação utilizando map() e outra utilizando 
#   filter(), comparando os resultados para verificar se são equivalentes. 

# 26.     [Dicionário] Utilize lambda para ordenar um dicionário com base 
#   em uma das suas chaves. 


# ------------

def f9():
    sum = lambda num1, num2: num1 + num2
    print(sum(10, 20))
    pass

# --------------------------

s = lambda x, y: x + y
s = lambda x, y: (x + y)
print(s(10,3))

for el in map(lambda x: x*3, range(1,11)):
    print(el)

names = ["fernanda", "luzia", "anne", "paula"]
for n in map(lambda n: str.capitalize(n), names):
    print(n)

names_upper = []
for n in map(lambda n: str.upper(n), names):
    names_upper.append(n)

print(names_upper)
for n in map(lambda n: str.lower(n), names_upper):
    print(n)

names_orderned = sorted(list(map(lambda n: str.capitalize(n), names)), reverse=True)
print(names_orderned)

names_orderned = sorted(names, key=lambda n:n)
print(names_orderned)

people = [
    {"name":"Lucy"},
    {"id":1,"name":"Zenny"},
    {"id":2,"name":"Carmen"},
    {"id":3,"name":"Yasmin"},
    {"id":4,"name":"Wiiliam"},
    {"id":5,"name":"Anderson"},
    {"id":6,"name":"Bernard"},
    {"id":7,"name":"Anne"}
]

people_ordened = sorted(people, key=lambda p: p["name"])
print(people_ordened)

nums = [5,6,4,7,3,8,2,9,1,0]
cube = map(lambda x: x ** 3, nums)

for el in sorted(map(lambda x: x ** 3, nums)):
    print(el)

print(cube)
cube = list(map(lambda x: x ** 3, nums))
print(cube)

# filter

evens = filter(lambda x: x % 2 == 0, nums)
print(list(evens))
odds = filter(lambda x: x % 2 != 0, nums)
print(list(odds))

# reduce (reduzir escrita de funções)

from functools import reduce

nums = [5,6,4,7,3,8,2,9,1,0]
sum_nums = reduce(lambda x, y: x + y, nums)
print(sum_nums)

sum_nums = reduce(lambda x, y: x + y, map(lambda x : x * 3, nums))
print(sum_nums)

# max number:
max_value = reduce(lambda x,y : x if x > y else y, nums)
print(max_value)

# min number:
min_value = reduce(lambda x, y: x if x < y else y, nums)
print(min_value)

# o que começam com a letra "A"
letter_a = filter(lambda p: p["name"][0] == "A", people)
print(list(letter_a))

# o que começam com a letra "A" usando map
letter_a = map(lambda p: p["name"][0] == "A", people)
print(list(letter_a)) 

# lambda com condicional:
d = lambda x, y: x / y if y != 0 else "Não se divide por zero."
print(d(10,0))

# ---------------------


sum = lambda x, y : x + y
print(sum(1,2))

mlt = lambda x, y: x * y
print(mlt(3,9))

pwr = lambda x,y: x**y
print(pwr(2,3))

for el in map(lambda x: x * 3, range(1, 10+1)):
    print(el, end=", ")

data = ["jdashdjs", "hjashdjas", "yeuqwyeuwy", "uewqiueiwq", "iuiwquiew"]
for el in map(lambda x: str.capitalize(x), data):
    print(el)
for el in map(lambda x: str.upper(x), data):
    print(el)

print(sorted(list(map(lambda x: str.upper(x), data)), reverse=True)) # para poder imprimir ordenado

people = [
    {"id":1,"name":"Anderson"},
    {"id":2,"name":"Fernanda"},
    {"id":3,"name":"Bianca"},
    {"id":4,"name":"Joana"},
    {"id":5,"name":"Anne"},
    {"id":6,"name":"Sara"},
    {"id":7,"name":"Lucy"},
]

list_ordened_by_name = sorted(people, key=lambda x: x["name"])
for el in list_ordened_by_name:
    print(f"ID:{el["id"]} | NAME:{el["name"]}")

nums = [5,6,4,7,3,8,2,9,1,0]
x3 = map(lambda x: x * 3, nums)
print(list(x3))

true_false = map(lambda x: x % 2 == 0, nums)
print(list(true_false))

odd = filter(lambda x: (x % 2 == 0), nums)
print(list(odd))

from functools import reduce

sum_nums = reduce(lambda x,y: x+y, nums)
print(sum_nums)

nums.remove(0) # removo o zero
mlt_nums = reduce(lambda x,y: x*y, nums)
print(mlt_nums)

print(min(3,1)) # o menor numero
print(max(1,3)) # o maior numero

# o maior item da lista:
max_value = reduce(lambda x,y: x if x > y else y, nums)
print(max_value)

x2 = list(map(lambda x: x*2, nums))
print(x2)

maior_numero_da_lista = reduce(lambda x,y: x if x > y else y, nums)
print(maior_numero_da_lista)

x5 = list(map(lambda x: x*5, nums))
print(x5)

class CalcLambda:
    def sum(self, x, y):
        f = lambda x, y : x + y
        return f(x, y)
    def sub(self, x, y):
        f = lambda x, y : x - y
        return f(x, y)
    def mlt(self, x, y):
        f = lambda x, y : x * y
        return f(x, y)
    def div(self, x, y):
        f = lambda x, y : x / y
        return f(x, y)
    def mod(self, x, y):
        f = lambda x, y : x % y
        return f(x, y)
    def __enter__(self):
        return self
    def __exit__(self, v1, v2, v3):
        pass
    
x, y = 10, 5
print(f"SUM: {CalcLambda().sum(x, y)}")
print(f"SUB: {CalcLambda().sub(x, y)}")
print(f"MLT: {CalcLambda().mlt(x, y)}")
print(f"DIV: {CalcLambda().div(x, y)}")
print(f"MOD: {CalcLambda().mod(x, y)}")

with CalcLambda() as crud:
    print(f"WITH SUM: {crud.sum(x,y)}")

scores = [[3,2,1],[4,5,6],[9,8,7]]

result = map(lambda x: x[2]*3, scores)
print(list(result))

people = [
    {"id":1,"name":"Anderson"},
    {"id":2,"name":"Fernanda"},
    {"id":3,"name":"Bianca"},
    {"id":4,"name":"Joana"},
    {"id":5,"name":"Anne"},
    {"id":6,"name":"Sara"},
    {"id":7,"name":"Lucy"},
]

print(list(map(lambda x: x["id"], people)))

# começa com a letra A:
print(list(filter(lambda x: x["name"][0] == "A", people)))

# com ID em par:
print(list(filter(lambda x: x["id"] % 2 == 0, people)))

# multiplas listas:
list1 = [1,2,3,4,5]
list2 = [6,7,8,9,0]

list_additions = map(lambda x,y:x*y, list1, list2)
print(list(list_additions))

# --------------------------------------------

# REVISAO:

nums = [1,2,3,4,5,6,7,8,9,0]

result = map(lambda x: x % 2 == 0, nums) 
print(list(result)) # [False, True, False, True, False, True, False, True, False, True]

result = filter(lambda x: x % 2 == 0, nums) 
print(list(result)) # [2, 4, 6, 8, 0]

from functools import reduce

result = reduce(lambda x, y: x if x > y else y, nums)
print(result) # 9 

words = ['jdsahjd','ieuqwiuew','oeqowieoqw','yeqwuyeuw']
print(words)
print(list(map(lambda w: w.capitalize(), words)))
print(list(map(lambda w: w.upper(), words)))

print(max(nums))
print(min(nums))

for i in map(lambda x: x * 5, range(1,11)):
    print(i, end=", ")
print("\n")

nums = [5,6,4,7,3,8,2,9,1,0]
print(sorted(filter(lambda x: x % 2 == 0, nums)))
print(sorted(filter(lambda x: x % 2 != 0, nums)))

people = [
    {"id":1,"name":"Anderson"},
    {"id":2,"name":"Fernanda"},
    {"id":3,"name":"Bianca"},
    {"id":4,"name":"Joana"},
    {"id":5,"name":"Anne"},
    {"id":6,"name":"Sara"},
    {"id":7,"name":"Lucy"},
]

print(sorted(people, key=lambda x: x["name"]))

for p in sorted(people, key=lambda x: x["name"]):
    print(p)

# multiplas listas:

list1 = [1,2,3,4,5]
list2 = [6,7,8,9,0]

# 1 x 2 | 2 x 7 | 3 x 8 | 4 x 9 | 5 x 0

list_add = map(lambda x, y: x * y, list1, list2)
print(list(list_add))

# ---------------------------------


from time import sleep as temporizador

def metodo(x, y):
    operacoes = [
        ("Somando", lambda a, b: a + b),
        ("Subtraindo", lambda a, b: a - b),
        ("Multiplicando", lambda a, b: a * b),
        ("Dividindo", lambda a, b: a / b if b != 0 else "Erro: divisão por zero!"),
        ("Modelando", lambda a, b: a % b if b != 0 else "Erro: módulo por zero!"),
        ("Potencializando", lambda a, b: a ** b),
    ]

    for nome, func in operacoes:
        print(f"{nome}: x = {x} e y = {y} ...")
        temporizador(0.5)
        yield func(x, y)

# Executando
execucao = metodo(10, 2)
opc = 1

if opc == 1:
    for _ in range(6):
        try:
            print(f"Resultado: {next(execucao)}")
            temporizador(2)
        except StopIteration:
            break
else:
    for resultado in execucao:
        print(f"Resultado: {resultado}")
        temporizador(2)

print("Todos os cálculos feitos!")
