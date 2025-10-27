try:
    try:
        file = open("hello.txt", "w")
        file.write("Hello, World!")
        file.close()
        file = open("dads.txt", "r")
        print(file.readline())
        file.close()
    except FileNotFoundError:
        print("Error: File not found.")
    except FileExistsError:
        print("Error: File not exists.")
except Exception:
    print("Error: Generic error.")

# ----------
    
import os

def Escrever():
    try:
        os.remove('file.txt')
    except  :
        print("Erro ao apagar arquivo.")
    
    arquivo = open('file.txt', 'w')
    getAtributos(arquivo)
    arquivo.write("Hello, World!")
    print(arquivo.seek(0, 0))
    arquivo.close()
    getAtributos(arquivo)

def Ler():
    arquivo = open('file.txt', 'r+')
    getAtributos(arquivo)
    print(arquivo.tell())
    for item in arquivo.readlines():
        print(item)
    arquivo.close()
    getAtributos(arquivo)

def Renomear():
    try:
        arquivo = os.rename('file.txt', 'arquivo.txt')
    except  :
        print("Erro ao renomear arquivo.")

def CriarExcluir():
    try:
        arquivo = open('file1.txt', 'w')
        os.remove(arquivo)
    except:
       pass

def GetCurrentDir():
    print(os.getcwd())

def MudarDirCurrent():
    try:
        os.chdir("newdir")
    except:
        pass

def CriarDiretorio():
    os.mkdir("Diretorio")

def DeleteDir():
    os.rmdir("Diretorio")

def getAtributos(arquivo):
    print("--------------------------------------------")
    print(arquivo.closed)
    print(arquivo.mode)
    print(arquivo.name)
    #print(arquivo.softspace)
    print("--------------------------------------------")
    
Escrever()
Ler()
Renomear()
CriarExcluir()
GetCurrentDir()
CriarDiretorio()
DeleteDir()
MudarDirCurrent()



