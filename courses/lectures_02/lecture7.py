# Lecture 07 

# Conceitos sobre o uso de arquivo em Python. 

#    1. Criar um código que exemplifique a execução da leitura de um arquivo 
#       de texto utilizando os métodos read() e readline(). 

file = open("lorem.txt", "r")
print(file.read())
file.close()

#    2.  Criar um código que exemplifique a execução da escrita em um arquivo 
#       de texto utilizando buffer e codificação para esse mesmo arquivo. 

file = open("file.txt", mode="w", buffering=-1, encoding="utf-8")
file.write("Hello, World!")
file.close()

#    3. Criar um código que exemplifique a execução da leitura de um arquivo 
#       de texto, utilizando buffer e codificação para esse mesmo arquivo. 

file = open("file_buffer_enc.txt", mode="w", buffering=-1, encoding="utf-8")
file.write("Hello, World!")
print(file.encoding)
file.close()

#    4.  Criar um código que exemplifique a abertura de um arquivo, exibindo 
#       seu conteúdo e os dados como codificação, tipo (usando type()) e outros 
#       metadados disponíveis. 

file = open("file_buffer_enc.txt", mode="r", buffering=-1, encoding="utf-8")
print(type(file)) # <class '_io.TextIOWrapper'>
print(file.encoding)
file.close()

#    5. Criar um código que exemplifique a abertura de um arquivo e o uso do 
#       read() diretamente dentro da função print(). 

print(open("lorem1.txt", "r").read()) # leitura completa
print(open("lorem1.txt", "r").readline()) # so uma linha

#    6. Criar uma lista de nomes de pessoas. 

people = ["Anderson", "Fernanda", "Luiza", "Caroline", "Sara", "Ava"]

#    7. Criar um código que exemplifique a inclusão desses nomes, um por um 
#       e separados por espaço, em um arquivo. 

file = open("people.txt", "w")
for p in people:
    file.write(f"{p}, ")
file.close()

#    8. Criar um código que exemplifique a leitura dos N primeiros caracteres 
#       de um arquivo, com o valor de N informado diretamente no print(). 

print(f"{open("lorem.txt", "r").read(5)}")

#    9. Criar uma classe que contenha métodos para trabalhar com arquivos, 
#       contendo os seguintes métodos: escrita, leitura, verificação se uma 
#       determinada palavra existe, e exclusão do arquivo. Todos os métodos 
#       devem conter tratamento de exceção. 

class TextEditor:

    def __init__(self, file):
        self.file = file

    def write_file(self, param):
        try:
            with open(file=self.file, mode="w", buffering=-1, encoding="utf-8") as file:
                file.write(param)
                file.close()
            print("Succesfully writed.")
        except Exception as err:
            print(f"Error: {err}")

    def read_file(self):
        try:
            with open(file=self.file, mode="r", buffering=-1, encoding="utf-8") as file:
                print(file.read())
                file.close()
        except Exception as err:
            print(f"Error: {err}")

    def find_in_file(self, param):
        try:
            with open(file=self.file, mode="r", buffering=-1, encoding="utf-8") as file:
                data = file.read()
                if data.find(param) != -1:
                    print("Exists.")
                else:
                    print("No exists.")
                file.close()
        except Exception as err:
            print(f"Error: {err}")

    def delete_file(self):
        try:
            import os
            os.remove(self.file)
            print("Succesfully deleted.")
        except Exception as err:
            print(f"Error: {err}")

    def __enter__(self):
        return self
    
    def __exit__(self,v1,v2,v3):
        pass

with TextEditor("text.txt") as obj:
    obj.write_file("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.")
    obj.read_file()
    obj.find_in_file("eiusmod")
    obj.delete_file()

language = "Java Language"
language = language.replace("Java", "Python")
print(language)
