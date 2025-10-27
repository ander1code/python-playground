i = 0
while(i < 10):
    print(i)
    i = i + 1

i = 0
while True:
    if i == 10:
        print("Finish!")
        break
    i+=1

i = 0
vet = [1,2,3,4,5,6,7,8,9,0]
while i < len(vet):
    if i == 4:
        print("X")
        i+=1
        continue
    print(vet[i])
    i+=1

people = ["Fernanda", "Alice", "Paula", "Caroline", "Vanessa"]
i = (len(people) - 1)
while i >= 0:
    print(people[i])
    i-=1

tuple = (0, 3, 6, 9, 12, 15, 18, 21, 24, 27)
while i < len(tuple):
    print(tuple[i])
    i+=1

for el in tuple:
    print(el) # nao preciso colocar o indice para imprimir.

for person in people:
    print(person)

name = "Anderson"
for char in name:
    if char == 's':
        print(" ")
        continue
    print(char)

for el in range(10):
    if (el % 2) == 0:
        print(el)

print(" ---------------- ")

for el in range(5, 10):
    if (el % 2) == 0:
        print(el)

print(" ---------------- ")

for el in range(1, 10, 3): # de 1 a 10, incrementando em 3.
    print(el) # nao imprimirá o 10.

nums = range(7)
for el in nums:
    print(el)

i = 0
nums = range(7) # iniciará em ZERO.
while i < len(nums):
    print(nums[i])
    i+=1

# while True:
#     pass

