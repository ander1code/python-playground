# LIST:

#     1.Crie uma lista com números desordenados. 

array = [7,6,8,5,9,3,0,2,1,4]

#    2. Crie um código que exemplifique a utilização dos métodos sort() e 
#       reverse() para ordenar e inverter a lista. 

array.sort()
print(array)
array.sort(reverse=True)
print(array)

#     3.Crie uma cópia da lista anterior utilizando copy() e, em seguida, 
#       adicione um item a essa lista copiada com append(). 

array.append(18273182732)
print(array)

#    4. Crie um código que exemplifique o uso do método pop() para remover 
#       um item da lista criada. 

array.pop()
print(array)

#     5.Crie um código que exemplifique a inserção de um item em um índice 
#       específico da lista, utilizando o método  insert(). 

array.insert(5, 777)
print(array)

#     6.Crie um código que aplique o método clear() na lista e, 
#       posteriormente, imprima a lista para confirmar que ela está vazia. 

array.clear()
print(array)

#    7.Crie um código que exemplifique a obtenção da primeira ocorrência de 
#       um determinado item na lista, utilizando o método  index(). 

array = [7,6,8,5,9,3,2,6,7,8,1,3,4,0,2,1,4]
print("\n", array.index(1))

#     8.Crie uma segunda lista de números. 

list1 = [7,6,8,5,9]
list2 = [3,0,2,1,4]

#     9.Crie um código que utilize a segunda lista para estender a primeira, 
#       utilizando o método extend(). 

list1.extend(list2)
print(list1)

# ---------------------

list = [5, 6, 4, 7, 3, 8, 2, 9, 1, 0]
list.sort()
print(list)

list.reverse()
print(list)

list.sort()

list_copy = list.copy()
list_copy.append("X")
print(list_copy)
print(list)

list.pop()
print(f"{list}")

list = [5, 6, 4, 7, 3, 8, 2, 9, 1, 0]

list.insert(5, 4251421)  # inserir na posição: 5, o valor: 4251421;
print(f"{list}")

list.clear()
print(list)

list = [5, 6, 4, 7, 3, 8, 2, 9, 1, 0]

print(len(list))

print(list.index(8)) # primeira posicao que aparece o 8;

list1 = list.copy()
list2 = [321,545,786,111,999]
list1.extend(list2) # junto uma lista noutra;
print(list1)

list = [5, 6, 4, 7, 3, 8, 2, 9, 1, 0]

# ---------------------

people = [
    "Anderson",
    "Fernanda",
    "Renata",
    "Cristiane",
    "Francine",
    "Joana"
]

for i in range(len(people)):
    print(f"{i} - {people[i]}")

# ----------------------
    
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']

print(fruits.count('apple'))

print(fruits)

print(fruits.reverse())

print(fruits.sort())

print(fruits.pop())


# ----------------------


def f1():
    print("Hello, world!")
    num = 3.14159
    name = "Anderson"
    lpeople = ['Anderson', 'Sarah', 'Lucy', 'Anne']
    tpeople = ('Anderson', 'Sarah', 'Lucy', 'Anne')
    colors = {
        1: 'Green',
        2: 'Yellow',
        3: 'Blue',
        4: 'White',
        5: 'Red'
    }
    del num, name, lpeople, tpeople, colors
    pass

def f2():
    people1 = ['Tiffany', 'Sarah', 'Lucy', 'Anne']
    people2 = ['Anderson', 'Jason', 'Steve']
    print(people1[:2])
    print(people1[2:3])
    print(people1 + people2)
    print(people1 * 2)
    # print(people1 + 'MARY')
    pass


def f4():
    for item in 'Hello, world!':
        print(item)
    
    for color in ['green', 'yellow', 'blue', 'white', 'red']:
        print(color)

    for num in range(0,9):
        print(num)
    
    for num in range(9,-1,-1):
        print(num)
    
    colors = ['green', 'yellow', 'blue', 'white', 'red'] 
    for index in range(0, len(colors)):
        print(colors[index])
    
    pass

def f5():
    print("ID: %d | Name: %s" %(123,'Anderson'))
    latim = """Lorem \nipsum dolor sit amet, consectetur adipiscing elit, 
    sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
    Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris 
    nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in 
    reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla 
    pariatur. \tExcepteur sint occaecat cupidatat non proident, sunt in 
    culpa qui officia deserunt mollit anim id est \nlaborum.""" 
    print(latim)
    print(u'Hello, World!')
    pass


def f6():
    colors = {
        1: 'Black',
        2: 'Red'
    }
    print(colors)
    colors.clear()
    colors = {
        1: 'Green',
        2: 'Yellow',
        3: 'Blue',
        4: 'White',
        5: 'Red'
    }
    colors[1] = 'Magenta'
    print(colors)
    del colors
    pass


# --------------------------

def fList():
    list = [True, 'A', "Anderson", (3 + 3j), ["green", "yellow"],  {'1':"Anderson"}, (1,2,3)]
    print(list)
    print(list[3])
    print(list[:3])
    print(list[3:])
    print(list * 2)
    print(list[:7] + [1,2,3])


# ---------------------------
    
def flist():
    vlist = ['Anderson', 'Sarah', 'Anne', 'Lucy', 'Tiffany', 'Anne']

    print(vlist)

    vlist[0] = 'Gina'

    print(vlist)

    print(vlist[0])
    print(vlist[:1])
    print(vlist[3:])

    for i in range(len(vlist)):
        print(vlist[i])

    for p in vlist:
        print(p)

    print("Quantidade: %d" % (len(vlist)))
    print("Máximo: %s" % (max(vlist)))
    print("Mínimo: %s" % (min(vlist)))
    print(list(('hdgsjhdgasjh', 'jhgsteuw', 'uywuyeuw', 'jasdodasldl')))

    print(list.count(vlist, 'Anne'))
    # print(vlist.index(1))
    print(vlist.append('Jacque'))
    # print(list.extend(vlist))
    print(list.insert(vlist, 6, 'Ava'))
    print(vlist.remove('Sarah'))
    # print(vlist.pop(obj = vlist[-1]))

    print(vlist.reverse())
    print(vlist)

    print(vlist.sort())
    print(vlist)

    del vlist

    try:
        print(vlist)
    except Exception as e:
        print('Lista já não está mais referenciada.')
    return
