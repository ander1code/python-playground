# Recursão

# loop ao contrario:

print("descendente:")

def recursion(n):
    if n == 0:
        return
    print(n)
    recursion(n - 1)

recursion(10)

print("ascendente:")

def recursion(n):
    if n == 10:
        return
    print(n)
    recursion(n + 1)

recursion(0)
