#Importando a biblioteca tkinter
#Na versão antiga é "from Tkinter import *" (Maiusculo)
from tkinter import *

janela = Tk()

Label(janela, text='Hello, World!').pack()
janela.mainloop()