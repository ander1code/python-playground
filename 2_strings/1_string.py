# STRING

message = "Hello, World!"
print(message.upper())
print(message.lower())
print(message.capitalize())

words = message.split()
print(words)

new_message = " ".join(words) # pode ser usado para desmembrar o split e juntar numa string.
print(new_message)

words = ["Hello", ", ", "World", "!"]
new_message = " ".join(words)

print(new_message.count("l"))

translate = message.replace("World", "Mundo")
print(translate.replace("Hello", "Olá"))

message = " Hello, World! "
print(message.strip())
print(message.rstrip())
print(message.lstrip())

files = ["file.txt", "file.mp3"]

for file in files:
    if file.endswith(".txt"):
        print("TXT file.")
    else:
         print("MP3 file.")

print(files[0].startswith("file"))

message = "Hello, World!"

print(message[7:len(message)])
print(message[0:5])

id = 123
name = "Anderson"
result = "ID: {} | NAME: {}".format(id, name)
print(result)
result = f"ID: {id} | NAME: {name}"
print(result)

print(message.find("World"))

# ---------------------------------------------------------------------

# String 

#                           Métodos e propriedades utilizadas em strings. 

#    1. Criar uma variável que contenha a seguinte frase: “Hello, World!”. 

message = "hello, world!"
print(message)

#    2.  Criar um código que exemplifique a utilização dos seguintes métodos: 

#       •    upper() 

print(message.upper())

#       •    lower() 

print(message.lower())

#       •    capitalize() 

print(message.capitalize())

#       •    split() 

print(message.split(","))

#       •    join() (para juntar strings em uma lista). 

message = ["Hello", ",", " World", "!"]
print("".join(message))

#    3. Criar um código que exemplifique a impressão da quantidade de um 
#       caractere específico contido em uma string, utilizando count(). 

count = message.count("h")
print(count)

#    4. Criar um código que exemplifique a utilização do replace() para 
#       substituir uma string dentro de outra. 

message = "Hello, World!"
print(message.replace("Hello", "Olá"))

#    5. Crie uma string sem uma formatação padrão, por exemplo: “ Hello,  
#       World! “. 

message = " Hello, World! "

#    6. Criar um código que exemplifique o uso dos seguintes métodos: 

#       • rstrip() 

print(message.rstrip())

#       • lstrip() 

print(message.lstrip())

#       • strip(). 

message = " Hello, World! "
print(message.strip())

#    7. Crie uma lista de nomes de arquivos com extensão “.txt” e “.mp3”. 


files = ["file1.txt","fbin.bin","file2.conf", "fmusic.mp3","file3.txt"]

#    8. Criar um código que exemplifique o seguinte: ao iterar sobre essa lista 
#       de nomes de arquivos, verifique se o nome do arquivo corrente é do 
#       tipo “.txt” ou “.mp3”, utilizando endswith(), e imprima uma 
#       mensagem. 

m,t=0,0
for f in files:
    if f.endswith(".mp3"):
        print("MP3 file.")
        m+=1
    if f.endswith(".txt"):
        print("TXT file.")
        t+=1

print(f"mp3: {m}")
print(f"txt: {t}")


# 9. Criar um código que exemplifique o seguinte: utilizando a lista de 
#    arquivos criada anteriormente, verifique se o nome começa com um 
#    determinado critério, utilizando startswith(). 

cont=0
for f in files:
    if f.startswith("file"):
        cont+=1

print(f"count: {cont}")

# 10. Criar um código que exemplifique a impressão da string criada 
#    anteriormente, porém a partir de um início e fim estipulados para a 
#    impressão dessa mesma string, utilizando a notação de slicing 
#    [início:fim]. 

print(message[8:len(message)-2])

# 11.      Criar um código que exemplifique as seguintes formas de 
#    impressão de variáveis dentro de uma string: 

id = 123
name = "Anderson"

#    •     "{}".format(variável) 

print("ID: {} | NAME: {}".format(id,name))

#    •     f" {variável}" 

print(f"ID: {id} | NAME: {name}")

#    •     "Dado: " + variável. 

print("ID:", id, "|", "NAME:", name)

# 12. Criar um código que exemplifique o uso do find() em uma string para 
#    encontrar a primeira ou única ocorrência de um item passado como 
#    argumento. 

print(message.find("Anderson"))

# --------------

def f3():
    str = 'Hello World!'
    print(str)          # Prints complete string
    print(str[0])      # Prints first character of the string
    print(str[2:5])     # Prints characters starting from 3rd to 5th
    print(str[2:])      # Prints string starting from 3rd character
    print(str * 2)      # Prints string two times
    print(str + "TEST") # Prints concatenated string
    pass

# --------------

def fString():
    str = "Hello, World!"
    print(str)
    print(str[3])
    print(str[:3])
    print(str[3:])
    print(str * 2)
    print(str[:7] + "World!")

# --------------

def fstring():
    str = "Hello, World!"
    print(str)
    print(str[3])
    print(str[:3])
    print(str[3:])
    print(str * 2)
    print(str[:7] + "World!")
    print(r'C:\\Windows')
    print('C:\\Windows')
    return