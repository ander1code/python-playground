import datetime

datas = [123, "Anderson", 'M', 4215421.11, True, datetime.date]
datas[0] = 432
print(datas)
print(datas[1])
print(type(datas))
print(len(datas))
print(datas[1:1]) # nao mostra nada!
print(datas[1:2])
# datas.sort() # Erro 
# print(datas) 


list = [6,5,4,7,2,8,1,9,0,3]
list.sort()
print(list)
list.sort(reverse=True)
print(list)
list.reverse()
print(list)
list.append(777)
print(list)
list.reverse()
list.insert(4,321)
print(list)

list.sort()
list.remove(3) # remove o primeiro "3"
print(list)
list.pop(7) # remove o que ta na posição. Numero: 8
print(list)

tuple = (5,4,3,2,1,0)
print(tuple)
print(type(tuple))
print(tuple[3])
print(tuple[2:4])
print(tuple.index(2))
print(tuple.count(2)) # conta a quantidade de itens mencionado, no caso é o 2.

names = []
name1 = input("Enter name 1: ")
name2 = input("Enter name 2: ")
name3 = input("Enter name 3: ")
names.append(name1)
names.append(name2)
names.append(name3)
names.sort()
print(names)


# Da erro:
"""
names = ()
name1 = input("Enter name 1: ")
name2 = input("Enter name 2: ")
name3 = input("Enter name 3: ")
names.append(name1)
names.append(name2)
names.append(name3)
names.sort()
print(names)
"""

list1 = ['r','a','d','a','r']

copy1 = list1.copy()
copy1.reverse()

if(copy1 == list1):
    print("Palindrome!!!")
else:
    print("Not palindrome.")

    