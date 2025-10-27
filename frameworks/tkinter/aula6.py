from tkinter import *

janela = Tk()
lb = Label(janela, text='Nenhum clique.')
    
lb.place(x=100, y=150)

i = 0
def btn_click():
    global i
    global lb
    i+=1
    if(i == 1):
        lb['text'] = 'Botão clicado %d vez.' %(i)
    else:
        lb['text'] = 'Botão clicado %d vezes.' %(i)

for i in range(1,1000):
    btn_click()

bt = Button(janela, text='EXECUTAR', command=btn_click)
bt.place(x=100, y=180)
janela.geometry('300x300+150+150')
janela['bg'] = 'green'
janela.mainloop()


