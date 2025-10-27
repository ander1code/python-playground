def greeting(name="Anderson"):
    return "Hello, " + name + "!"

data = print(greeting("Mara"))
print(data) # None

print(greeting())

print("Hello", " ", end="Anderson!")

# ----------------------

tuple = ("Anderson", "Lucia", "Fernanda", "Mara", "Tania")

def print_len(collection):
    print(len(collection))

def print_items(collection):
    for el in collection:
        print(el, end=" ")

print_len(tuple)

print_items(tuple)   

# ----------------------

print("\n")

def calc_fact(f,n):
    for i in range(1, n+1):
        f*=i
        print(f)

calc_fact(1,5)


def calc_dollar_real(dollar):
    val_real = 5.87
    print("value: R$",(val_real * dollar))

calc_dollar_real(7)

def show():
    return # None

print(show())

# ----------------------

def show(n):
    if n==0:
        return
    print(n)
    show(n-1)

show(10)

# ----------------------

def calc_fact(n):
    if((n==0)or(n==1)):
        return 1
    return calc_fact(n-1) * n # 1 x 2 x 3 x 4 x 5 = 120

print(calc_fact(5))

# ----------------------

def calc_fact(n):
    if((n==0)or(n==1)):
        return 1
    return calc_fact(n-1) + n # 1 + 2 + 3 + 4 + 5 = 15

print(calc_fact(5))

# ----------------------

people = ["Anderson", "Lucia", "Fernanda", "Mara", "Tania"]

def print_list(param, idx=0):
    if(len(param) == idx):
        return
    print(param[idx])
    print_list(people, idx+1)

print_list(people)
    