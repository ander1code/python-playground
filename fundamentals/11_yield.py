from time import sleep as temporizador
def metodo():
    print("Fazendo primeira coisa ...")
    temporizador(0.5)
    yield "\t - primeira coisa feita!"
    print("Fazendo segunda coisa ...")
    temporizador(0.5)
    yield "\t - segunda coisa feita!"
    print("Fazendo terceira coisa ...")
    temporizador(0.5)
    yield "\t - terceira coisa feita!"
    print("Tudo feito!") # nao executa!

execucao = metodo()

for el in range(0,3):
    print(next(execucao)) # next garante o avanço!
    temporizador(2)
print("Tudo feito!")


# -----------------------------------------------------

from time import sleep as temporizador
def metodo(x,y):
    print(f"Somando: x = {x} e y = {y} =  ...")
    temporizador(0.5)
    yield x + y
    print(f"Subtraindo: x = {x} e y = {y} ...")
    temporizador(0.5)
    yield x - y
    print(f"Multiplicando: x = {x} e y = {y} ...")
    temporizador(0.5)
    yield x * y
    try:
        print(f"Dividindo: x = {x} e y = {y} ...")
        temporizador(0.5)
        yield x / y
    except ZeroDivisionError:
        print("Não pode dividir por zero!")
    print(f"Modelando: x = {x} e y = {y} ...")
    temporizador(0.5)
    yield x % y   
    print(f"Potecializando: x = {x} e y = {y} ...")
    temporizador(0.5)
    yield x ** y   

execucao = metodo(10,2)

opc = 1

if opc == 1:
    print(next(execucao)) # next garante o avanço!
    temporizador(2)
    print(next(execucao)) # next garante o avanço!
    temporizador(2)
    print(next(execucao)) # next garante o avanço!
    temporizador(2)
    print(next(execucao)) # next garante o avanço!
    temporizador(2)
    print(next(execucao)) # next garante o avanço!
    temporizador(2)
    print(next(execucao)) # next garante o avanço!
    temporizador(2)
else:
    for el in range(0,7):
        try:
            print(next(execucao)) # next garante o avanço!
            temporizador(2)
        except:
            pass # trabalhar com next(), tem que colocar o try... except
    print("Todos os calculos feitos!")
