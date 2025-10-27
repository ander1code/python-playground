# factorial:

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return factorial(n - 1) * n

print(factorial(10))


# -------

def calc_fibonacci(a,b,l):
    while a < l:
        print(a, end=", ")
        a,b=b,a+b
    
calc_fibonacci(0,1,10)