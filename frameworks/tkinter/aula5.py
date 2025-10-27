from tkinter import *

#Gerenciadores:
# ---- place -> Menos utilizado (x e y).
# ---- Pack --> Empacota os componentes de forma vertical ou horizontal.
# ---- Grid --> Organiza os componentes como numa grade.

janela = Tk()
lb = Label(janela, text='Hello, World!!!')
    
#Utilizando o gerenciador de layout.
lb.place(x=100, y=100)
    
janela.geometry('500x400+150+150')
janela['bg'] = 'green'
janela.mainloop()


