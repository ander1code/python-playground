import math

import datetime


#Comentário teste.
#nome = "Anderson"
"""
Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
sed do eiusmod tempor incididunt ut labore et dolore magna 
aliqua. Ut enim ad minim veniam, quis nostrud exercitation 
ullamco laboris nisi ut aliquip ex ea commodo consequat. 
Duis aute irure dolor in reprehenderit in voluptate velit 
esse cillum dolore eu fugiat nulla pariatur. Excepteur 
sint occaecat cupidatat non proident, sunt in culpa qui 
officia deserunt mollit anim id est laborum.
"""
def Saudacao():
    print("Hello, World!!!")

def TestTrue():
    if True:
        print("Teste do IF")

##Trabalhando com variáveis:

def SumVariables():
    valor1 = 25
    valor2 = 10
    print(valor1+valor2)


def TestTypeVariables():
    #Descobrindo o tipo:
    varInt = 35
    varFloat = 3542.32
    varString = "Anderson"
    varChar = 'M'
    varBool = True

    print(type(varInt))
    print(type(varFloat))
    print(type(varString))
    print(type(varChar))
    print(type(varBool))

    #TESTE:
    teste_var = 1000
    print(type(teste_var))
    teste_var = 1000.35
    print(type(teste_var))


def PrintValues():
    codigo = 123
    nome = "Anderson"
    salario = 3241.54
    print("Código: " + str(codigo))
    print("Nome: %s" % nome)
    print("Salário: %.2f" % salario)
    print ("%.2f" % math.pi)


def InputAndPrint():
    ##input com string:
    nome = input("Informe o seu nome: ")
    print("Hello, %s !" %nome)


def PrintMathValues():
    print(10/6)
    print(10//6)
    print(type(10/6))
    print(type(10//6))
    print(5 % 3)
    print(5**3)

def TestIFElse():
    if(True):
        print("Verdadeiro")
    else:
        print("Falso")

    idade = 15
    if(idade >= 18):
        print("Permitido")
    else:
        if(idade < 18):
            print("Negado")

def funcao():
    soma = valor1 + valor2
    print(soma)
    print(booleano)
    sobrenome = "Conceicao"
    print(nome + ' ' + sobrenome)
    print(soma)


def OperadorRelacional01():
    idade = int(input("Informe a sua idade: "))

    if(idade <= 0):
        print("Sua idade não pode ser menor ou igual a zero")
    elif(idade > 150):
        print("Sua idade não pode ser acima de 150 anos.")
    elif(idade < 18):
        print("Sua idade não pode ser menor que 18 anos.")


def Impressao01():
    nome = "Anderson"
    idade = 35
    print("Meu nome é %s e tenho %d anos." %(nome, idade))


def OperadorLogico01():
    a = False
    b = True

    exp1 = a and b
    exp2 = a or b
    exp3 = a and not(b)
    exp4 = a is b  
    exp5 = a is not(b)
    #exp6 = a in b
    #exp7 = a not in b

    print("a and b = %s" % exp1)
    print("a or b = %s" % exp2)
    print("a and not(b) = %s" % exp3)
    print("a is b = %s" % exp4)
    print("a is not(b) = %s" % exp5)
    #print("a in b = %s" % exp6)
    #print("a not in b = %s" % exp7)

    #complementando
    print(type(54) is type(True))

def EstudoSobreBlocoPython():
    print("Estudo Sobre Bloco(espaçamentos) Python.")

def Atribuicao01():
   nome, sobrenome = "Anderson", "Conceição"
   print(nome) 
   print(sobrenome) 

def Atribuicao02():
   x, y, z = 2, 4 ,8
   a, b, c = x*2, x+y+z, x*y*z
   print(a) 
   print(b)
   print(c)

def Atribuicao03():
   x = 2
   print(x)
   x += 1
   print(x)
   x -= 1
   print(x)
   x *= 1
   print(x)
   x /+ 1
   print(x)
   x %= 1
   print(x)

def TrocandoValores01():
    #Não precisarei de um "TEMP".
    valor1 = 35
    valor2 = 41
    valor1, valor2 = valor2, valor1
    print("valor1 = %d" % valor1)
    print("valor2 = %d" % valor2)

def AtribuicaoCondicional01():
    x = 35
    mensagem = "Sim!" if x == 10 else "Não!"
    print(mensagem)

def AtribuicaoCondicional02():
    valor = int(input("Informe um número: "))
    mensagem = "Par" if (valor % 2) == 0 else "Impar"
    print(mensagem)

def While01():
    x = 0
    while(x <= 10):
        print("\n%d" % x)
        x += 1

def While02():
    x = 0
    while(x <= 10):
        print("\n%d" % x)
        x += 1
    else:
        print("Loop Finalizado.");

    print("FIM!");


def ForIn01():
    for c in "Anderson":
        print("\n%s" % c)

def Range01():
    print(type(range(0,10,2)))
    print(list(range(0,10,2)))
    print(list(range(0,10,1)))
    print(list(range(99)))

def Range02():
    print(list(range(100,0,-3)))
    print(list(range(-100,0,3)))

def forRange01():
    for item in range(100,0,-3):
        print(item)  

def Break01():
    for item in range(100,0,-2):
        if(item == 50):
            print("Anterior %d." % (item + 2))
            print("Terminou em 50!!!") 
            break  
    
    print("Fora do Laço FOR!!!")  

def Continue01():
    print("INÍCIO")
    i = 0
    while (i < 100):
        i+=1
        if(i % 2 == 0):
            continue #Paralisa um unico ciclo do Loop.
        if(i == 50):
            break
        print(i)    
    print("FIM")  

def Lista01():
    #São todos os elementos em conjunto separados por virgula e 
    #delimitados por colchetes.
    lista = [53,True,"Anderson", 4.65,'C']
    print(type(lista))
    print(type([]))
    for item in lista:
        print(item)
    
    print(lista[2])

    lista = list("Anderson")
    print(lista)
    for item in lista:
        print(item)
   
    lista = list(("Anderson"))
    print(lista)

    lista = list((6,5,4,3,2,1))
    print(lista)

    lista = list(("Anderson",))
    print(lista)

    variavel = (5)
    print(type(variavel))
    
    variavel = (5,)
    print(type(variavel))

def Lista02():
    lista = [['A','n','D'],['12','11','81'],[]]
    print(type(lista))
    print(lista[1][1])
    print("Tamanho da Lista: %d" % len(lista))
    print(lista[len(lista)-1])

def Lista03():
    lista = [2,3,4]
    lista = [1] + lista
    print(lista)
    lista = lista + [5]
    print(lista)
    lista = lista + [6,7,8,9]
    print(lista)
    lista = [0] + lista
    print(lista)
    lista.append(10)
    print(lista)
    lista.append(["Anderson",True,4.5,'M'])
    print(lista)
    del(lista[len(lista)-1])
    print(lista)
    lista1 = 10*[1]
    print(lista1)
    lista += lista1
    print(lista)
    print(50*'-')

def Interacao01():
    lista = [5,4,2,3,8,0,9,7,6,1]
    lista.sort()
    i = 0
    for item in lista:
        lista[i] *= 100
        i = i + 1    

    print(lista) 

def Interacao02():
    lista = list(range(10,-1,-2))
    print(lista)


def Interacao03():
    lista = [5,4,2,3,8,0,9,7,6,1]
    lista.sort()
    i = 0
    for i in range(len(lista)):
        lista[i] *= 100
        
    print(lista)

def Enumerate01():
    lista = ["Anderson", 35, 4598.54, 'M', True]
    varEnum = enumerate(lista)
    print(varEnum)
    lista = list(varEnum)
    print(lista)

def Enumerate02():
    lista = ["Anderson", 35, 4598.54, 'M', True]
    for idx, item in enumerate(lista):
        print(lista[idx])

def Fatiamento01():
    lista = list(range(1,10))
    print(lista[:3])   #1,2,3
    print(lista[7:])   #8,9
    print(lista[::3])  #1,4,7
    print(lista[7::])  #1,4,7
    print(lista[5::5]) #6
    print(lista[::-1]) #9,8,7,6,5,4,3,2,1
    lista_fatia = lista[0:len(lista):3]
    print(lista_fatia)
    
def Fatiamento02():
    nome = "Anderson"
    print(nome[:3])   #1,2,3
    print(nome[7:])   #8,9
    print(nome[::3])  #1,4,7
    print(nome[7::])  #1,4,7
    print(nome[5::5]) #6
    print(nome[::-1]) #9,8,7,6,5,4,3,2,1
    nome_fatia = nome[0:len(nome):3]
    print(nome_fatia)

def ElementosLista01():
    lista = [35,"Anderson", True, 4567.65]
    print(lista)
    
    lista.insert(3,'Conceição')
    print(lista)
    
    lista.append(5567.76)
    print(lista)
    
    print(lista.pop(-1))
    print(lista)
    
    del(lista[1:3])
    print(lista)

    lista.clear()
    print(lista)

def Ordenacao01():
    lista = ["zito", "João", "antonio", "Anderson"]
    lista.sort(reverse=True)
    print(lista)
    lista.sort(reverse=False)
    print(lista)
    lista.reverse()
    print(lista)

def TamanhoLista():
    lista = ["Anderson", 35, 4598.54, 'M', True]
    print(lista)
    print(len(lista))
    print(lista[len(lista)-1])
    lista.insert(4,"Hello, World!")
    print(lista)
    lista.append("cerveja")
    lista.insert(3,"cerveja")
    print(lista)
    print(lista.count("cerveja"))
    print(lista.index(True))

def Tupla01():
    tupla = tuple("Anderson")
    print(tupla)
    #Tupla => Conjunto de objetos separados por virgula.
    objeto = (1,2,3)
    print(type(objeto))
    objeto = True,"Anderson",35,4663.43,'M'
    print(type(objeto))
    #Não possui insert (Estado ReadOnly).

def In01():
    lista = [52,54,21]
    x = 54
    print(x in lista)

def In02():
    tupla = True,"Anderson",35,4532.12,'M'
    x = "Anderson"
    print(x in tupla)

def In03():
    numeros = (1,99,-81)
    x = 45
    print(x in numeros)

def In04():
    numeros = range(1,99)
    x = 100
    print(x in numeros)

def In05():
    numeros = range(0,10,3)
    x = 6
    if x in numeros:
        print("Verdadeiro")
    else:
        print("Falso")

def NotIn01():
    lista = [52,54,21]
    x = 54
    print(x not in lista)

def NotIn02():
    tupla = True,"Anderson",35,4532.12,'M'
    x = "Anderson"
    print(x not in tupla)
  
    
def And01():
    x = 1
    y = 81
    if(x and y in range(3,90,3)):
        print("Verdadeiro")
    else:
        print("Falso")

def And02():
    lista = [1,4,6,9,0,5,7]
    resultado = ((5 or 8) and (3 and 7) in lista)
    print(resultado)

def And03():
    resultado = ((5 or 8) and (3 and 7) in range(1,5))
    print(resultado)

def Or01():
    lista = [65,-35,76,-89,12,81,5,7,0,99]
    x = 50
    y = 81
    if(x or y in lista):
        print("Verdadeiro")
    else:
        print("Falso")

def In06():
    numero = int(input("Informe um numero: "))
    if(numero in [35,12,11,81]):
        print("Verdadeiro")
    else:
        print("Falso")

        
def In07():
    lista = [35,12,11,81,54,6,8,63]
    while True:
        numero = int(input("Informe um numero o '0' para sair: "))
        if(numero == 0):
            break
        if(numero in lista):
            print("Acertou.")
        else:
            print("Errou.")
    print("Terminado")

def String01():
    print('String com aspas simples.')
    
def String02():
    texto = "String com aspas duplas."
    print(texto) 

def String03():
    texto = '''hsagdhsagdsagdsagdjs
    jsahdjsahdkjsahdksahkjds
    kjdsahdjksahkdjsahkdjsa
    kdsahdjkshajkdshakjd'''
    print(texto)

def String04():
    texto = """hsagdhsagdsagdsagdjs
    jsahdjsahdkjsahdksahkjds
    kjdsahdjksahkdjsahkdjsa
    kdsahdjkshajkdshakjd"""
    print(texto)

def FatiandoString01():
    texto = "Para o Python, toda a lista e uma string imutável."
    print(type(texto[0]))
    print(type(texto))
    print(texto[-1]) #Ultimo elemento de uma string.
    print(texto[0:len(texto):3])
    print(texto[::-1])
    print(texto[::2])


def PropriedadesString01():
    texto = "Para o Python, toda a lista e uma string imutável."
    print(len(texto))
    print(len("Anderson"))
    print(len(""))
    #texto[7] = "Z" #Da "exception".
    texto_split = texto.split(" ")
    print(texto_split) #Gera uma lista com as palavras separadas por espaço.
    print(texto_split[2])
    print(texto_split[2] + " " + texto_split[9])
    print(texto.replace("a", "u"))
    print(id(texto.replace("a", "u")))

def CompararString01():
    #Comparação binária.
    print("A" > "a") 
    print("a" > "1")
    for i in range(122):
        print(str(i) + " - " + chr(i))
    print(ord("A")) #Número de A na tabelas ASCII.

def InteracaoString01():
    texto = "Anderson"
    for l in texto:
        print(l)

def InteracaoString02():
    i = 0;
    texto = "Anderson"
    while(i < (len(texto))):
        print(i, texto[i])
        i+=1

def InteracaoString03():
    texto = "Anderson"
    #Enumerate no texto:
    enum_texto = enumerate(texto)
    #Gerando dicionário com o Enumerate:
    print(dict(enum_texto))
    for k,v in enumerate(texto):
        print(k,v)

def Dicionario01():
    #No python, dicionário são todos os 
    #elementos delimitados por chaves {}.
    print("Tipo de Dicionários = ", type({}))
    ##########################
    d1 = dict()
    print("Tipo de d1 = ", type(d1))
    d1[0] = "verde"
    d1[1] = "amarelo"
    d1[2] = "azul"
    d1[3] = "branco"
    print(d1)
    ##########################
    d2 = {"nome":"Anderson","idade":35}
    print("Tipo de d2 = ", type(d2))
    print(d2)

def Dicionario02():
    d1 = dict()
    print("Tipo de d1 = ", type(d1))
    d1[0] = "verde"
    d1[1] = "amarelo"
    d1[2] = "azul"
    d1[3] = "branco"
    print("Quantidade de elementos = ", len(d1))
    print("Imprimindo um Item = ", d1[2])
    print("Chaves cadastradas = ", d1.keys())
    print("Itens cadastrados = ", d1.items())
    
    #Verificando existencia:
    print("vermelho" in d1)
    print("azul" in d1)

    #Excluindo um item por vez na interação.
    while (0 != len(d1)):
        print("Removendo = ", d1.popitem())
        print(d1)
    

def Dicionario03():
    #Dicionário 01:
    d1 = dict()
    d1[0] = "verde"
    d1[1] = "amarelo"
    print(d1)

    #Dicionário 02:
    d2 = {2:"azul", 3:"branco"} #mesmos indices, sobreposição.
    print(d2)
    
    #Atualizando Dicionario 01:
    d1.update(d2)
    print(d1)

    t = (4,5,6)
    d1[t] = "Isso é uma Tupla."
    print(d1)
    
    #l = [64,43,11]
    #d1[l] = "Lista não é permitido como chave."
    #print(d1)

def Calculadora(valor1, op, valor2):
    #A chamada so pode ocorrer apos o bloco de declaração.
    if(op == 1):
        return valor1 + valor2
    if(op == 2):
        return valor1 - valor2
    if(op == 3):
        return valor1 * valor2
    if(op == 4):
        return valor1 / valor2
    if(op == 5):
        return valor1 % valor2

def FuncaoParam01(valor1, valor2):
    print("valor1 = %d && valor2 = %d" % (valor1, valor2))

#def FuncaoParam01(valor1):
#    print("valor1 = %d" % valor1)

def FuncaoParam02(valor1=11, valor2=12):
    print("valor1 = %d && valor2 = %d" % (valor1, valor2))

def FuncaoParam03(valor2, valor1=11):
    print("valor1 = %d && valor2 = %d" % (valor1, valor2))

# *************************************************************** #

#Argumento Posicionais(Tupla).
def ArgPosicionais01(codigo, nome, dataNasc, sexo):
    print("Código: {} \nNome: {} \nData de Nascimento: {} \nSexo: {}".format(codigo, nome, dataNasc, sexo))

#Argumento Nomeados(Dicionário).
def ArgNomeados01(codigo, nome, dataNasc, sexo):
    print("Código: {} \nNome: {} \nData de Nascimento: {} \nSexo: {}".format(codigo, nome, dataNasc, sexo))

def CalculadoraMultReturn(valor1, valor2):
    #A chamada so pode ocorrer apos o bloco de declaração.
    soma = valor1 + valor2
    subt = valor1 - valor2
    mult = valor1 * valor2
    divs = valor1 / valor2
    modl = valor1 % valor2
    return soma, subt, mult, divs, modl 

def Potencia(valor):
    quadrado = valor**2
    cubo = valor**3
    return quadrado, cubo

#Receberá uma tupla de valores.
def ListaArgumentos01(*args):
    print(args)

def ListaArgumentosAssociativos(**kwargs):
    print(kwargs)

def Argumentos(*args, **kwargs):
    print(args)
    print(kwargs)


#---------------------------------------------------------------------------------#
#  Chamada das Funções                                                            #
#---------------------------------------------------------------------------------#

#Saudacao()
#TestTrue()
#SumVariables()
#TestTypeVariables()
#PrintValues()
#InputAndPrint()
#PrintMathValues()
#TestIFElse()
#funcao()
#OperadorRelacional01()
#Impressao01()
#OperadorLogico01()
#EstudoSobreBlocoPython()
#TrocandoValores01()
#Atribuicao01()
#Atribuicao02()
#Atribuicao03()
#AtribuicaoCondicional01()
#AtribuicaoCondicional02()
#While01()
#While02()
#ForIn01()
#Range01()
#Range02()
#forRange01()
#Break01()
#Continue01()
#Lista01()
#Lista02()
#Lista03()
#Interacao01()
#Interacao02()
#Interacao03()
#Enumerate01()
#Enumerate02()
#Fatiamento01()
#Fatiamento02()
#ElementosLista01()
#Ordenacao01()
#TamanhoLista()
#In01()
#In02()
#In03()
#In04()
#In05()
#NotIn01()
#NotIn02()
#And01()
#And02()
#And03()
#Or01()
#In06()
#In07()
#String01()
#String02()
#String03()
#String04()
#PropriedadesString01()
#CompararString01()
#InteracaoString01()
#InteracaoString02()
#InteracaoString03()
#Dicionario01()
#Dicionario02()
#Dicionario03()
#print(Calculadora(9,1,3))
#FuncaoParam01(81,35)
#FuncaoParam01(79)
#FuncaoParam02()
#FuncaoParam03(6,8)


#---------------------------------------------------------------------------------#
#  Chamada com Argumentos                                                         #
#---------------------------------------------------------------------------------#


#Será enviado uma tupla:
#ArgPosicionais01(123, "Anderson", datetime.date(1981,11,12), 'M')
#print("\n\n")

#Será enviado um dicionário:
#ArgNomeados01(nome="Anderson",  sexo='M', dataNasc=datetime.date(1981,11,12),codigo=123)
#print("\n\n")

#Híbrido:
#ArgNomeados01(123, "Anderson", dataNasc=datetime.date(1981,11,12), sexo='M')
#print("\n\n")

#print(Calculadora(12,3,8))

#Atribuindo em variáveis
#print("\n\n")
#a,b,c,d,e = CalculadoraMultReturn(10,5)
#print(a)
#print(b)
#print(c)
#print(d)
#print(e)

#print("\n\n")
##Atribuindo em somente um valor e gerando um TUPLA.
#t = CalculadoraMultReturn(4,2)
#print(type(t))
#print("\n\n")
#for item in t:
#    print(item)

#print("\n\n")
##Desempacotamento:
#a,b,c,d,e = t
#print(a)
#print(b)
#print(c)
#print(d)
#print(e)

#valor = 2
#resultado1, resultado2 = Potencia(valor)
#print("\n\n\n%d ao Quadrado = %d | %d ao Cubo = %d " % (valor, resultado1, 
#                                                        valor, resultado2))

#ListaArgumentos01("Anderson", 123, 5454.43, datetime.date(1981,11,12), 'M')
#ListaArgumentos01(1,2,3)
#ListaArgumentos01(True)

#ListaArgumentosAssociativos(nome="Anderson", codigo=123, renda=5454.43, dataNasc=datetime.date(1981,11,12), sexo='M')
#ListaArgumentosAssociativos(status=True)
#ListaArgumentosAssociativos(lista=(81,11,12))

#Argumentos("Anderson", 123, 5454.43, dataNasc=datetime.date(1981,11,12), sexo='M')
