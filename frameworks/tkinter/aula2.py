from tkinter import *

#tkinter = Tk Interface. Não faz parte do Python.
#Não recomendado para o uso no mercado. Possui poucos recursos.

#widget -> qualquer parte do projeto grafico. 
#container -> Onde está os widgets do projeto.
#       container possui widgets.

#top-level window -> Janela que se sobrepõe.
#frame -> Organização de uma janela.
#child-parent -> widget dentro de um container (por exemplo).
#parent-child -> container possui widgets (por exemplo).

janela = Tk()
Label(janela, text='Hello, World!').pack()
janela.mainloop()