import random

s = set()
for _ in range(0,100):
    s.add(random.randrange(1,11))

print(s, type(s))

s.clear()

print(s, type(s))


i = 0
while i < 10:
    if i == 5:
        print("X")
        i+=1
        continue
    else:
        print(i)
    i+=1

i = 0
names = "Anderson"
while i < len(names):
    if i == 4:
        print("X")
        i+=1
        continue
    else:
        print(names[i])
    i+=1


names = "Anderson"
i = len(names) - 1  # Começa do último índice (7)
while i >= 0:
    if i == 4:
        print("X")
    else:
        print(names[i])
    i -= 1

names = "Anderson"
for l in names:
    if l == "s":
        print("X")
        continue
    print(l)

print("jhdasjhdasjhdsjahdsjdhasj")

names = "Anderson"
i = 0
while i < len(names):
    if names[i] == "s":
        print("X")
        i+=1
        continue
    else:
        print(names[i])
        i+=1

for i in range(0,10):
    if i % 2 == 0:
        continue
    print(i)

i = 0
while i < 10:
    if i % 2 == 0:
        i+=1
        continue
    print(i)
    i+=1

while True:
    break

# -----------------------

def floop():
    cont = 0
    while cont < 10:
        print(cont)
        cont = cont + 1

    for n in range(0, 34, 3):
        print(n)

    print("\n\For aninhado:")

    list = [[3,6,8],[4,7,0],[-1,3,5]]
    for x in range(len(list)):
        for y in range(len(list[x])):
            print("[%d,%d] = %d" % ((x + 1), (y + 1), list[x][y]))

    print("\n\nWhile aninhado:")
    x = y = 0
    while x < len(list):
        while y < len(list[x]):
            print("[%d,%d] = %d" % ((x + 1), (y + 1), list[x][y]))
            y = y + 1
        x = x + 1
        y = 0
    return

# -----------------------

nums = [5,6,7,4,3,8,9,2,1,0]
nums_iter = iter(nums)

while True:
    try:
        print(next(nums_iter))
    except StopIteration as err:
        break

for _ in range(10):
    print("Hello, World!")

