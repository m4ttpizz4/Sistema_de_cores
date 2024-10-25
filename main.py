from tkinter import *
import tkinter.messagebox

#cores

cor0 = "#444466"  # Preta  [Black]
cor1 = "#feffff"  # branca [Withe]
cor2 = "#004338"

#Criando a janela

janela = Tk()
janela.geometry('530x250')
janela.configure(bg=cor1)

#Configurando a janela

tela = Label(janela, bg=cor0, width=40, height=10, bd=1)
tela.grid(row=0,column=0)

frame_direita = Frame(janela, bg=cor1)
frame_direita.grid(row=0,column=0)
 
frame_baixo = Frame(janela, bg='red')
frame_baixo.grid(row=1, column=0, columnspan=2, pady=15)

# Configurando a janela direita

l_red = Label(frame_direita,text='Red',width=7, bg=cor1, fg='red', anchor='nw', font=("Time New Roman", 12 ,"bold"))
l_red.grid(row=0,column=0)

s_red=Scale(frame_direita, from_=0, to=255, length=150, bg=cor1, fg="red", orient=HORIZONTAL)
s_red.grid(row=0, column=0)

janela.mainloop()