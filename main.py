from tkinter import *
import tkinter.messagebox

#função para atualizar a cor da tela:
def atualizar_cor(*args):
    r = s_red.get()
    g = s_green.get()
    b = s_blue.get()
    cor = f'#{r:02x}{g:02x}{b:02x}'
    tela.configure(bg=cor)

preto = "#444466"
branco = "#feffff"
#criando interface:
janela = Tk()
janela.geometry('530x250')
janela.configure(bg=branco)

#configurando a tela principal:
tela = Label(janela, bg=preto, width=40, height=10, bd=1)
tela.grid(row=0, column=0, columnspan=3)

#frame direita:
frame_direita = Frame(janela, bg=branco)
frame_direita.grid(row=1, column=0)

#frame baixo:
frame_baixo = Frame(janela, bg=branco)
frame_baixo.grid(row=2, column=0, columnspan=3, pady=15)

#vermelho:
l_red = Label(frame_direita, text='Vermelho', width=7, bg=branco, fg='red', anchor='nw', font=("Arial", 12, "bold"))
l_red.grid(row=0, column=0)
s_red = Scale(frame_direita, from_=0, to=255, length=150, bg=branco, fg="red", orient=HORIZONTAL, command=atualizar_cor)
s_red.grid(row=0, column=1)

#verde:
l_green = Label(frame_direita, text='Verde', width=7, bg=branco, fg='green', anchor='nw', font=("Arial", 12, "bold"))
l_green.grid(row=1, column=0)
s_green = Scale(frame_direita, from_=0, to=255, length=150, bg=branco, fg="green", orient=HORIZONTAL, command=atualizar_cor)
s_green.grid(row=1, column=1)

#azul:
l_blue = Label(frame_direita, text='Azul', width=7, bg=branco, fg='blue', anchor='nw', font=("Arial", 12, "bold"))
l_blue.grid(row=2, column=0)
s_blue = Scale(frame_direita, from_=0, to=255, length=150, bg=branco, fg="blue", orient=HORIZONTAL, command=atualizar_cor)
s_blue.grid(row=2, column=1)

#iniciando o loop principal:
janela.mainloop()