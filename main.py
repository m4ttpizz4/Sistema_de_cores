#bibliotecas:
from tkinter import *
import tkinter.messagebox

#função para atualizar cor da rolagem:
def atualizar_cor(*args):
    r = s_red.get()
    g = s_green.get()
    b = s_blue.get()
    cor = f'#{r:02x}{g:02x}{b:02x}'
    tela.configure(bg=cor)

#função para alternar a cor do tema:
def toggle_dark_mode():
    global dark_mode
    if dark_mode:
        janela.configure(bg=preto)
        tela.configure(bg=preto)
        frame_direita.configure(bg=preto)
        frame_baixo.configure(bg=preto)
        l_red.configure(bg=preto)
        l_green.configure(bg=preto)
        l_blue.configure(bg=preto)
        s_red.configure(bg=preto)
        s_green.configure(bg=preto)
        s_blue.configure(bg=preto)
        dark_mode_button.configure(text="Dark Mode")
        dark_mode = False
    else:
        janela.configure(bg=preto)
        tela.configure(bg=branco)
        frame_direita.configure(bg=preto)
        frame_baixo.configure(bg=preto)
        l_red.configure(bg=preto)
        l_green.configure(bg=preto)
        l_blue.configure(bg=preto)
        s_red.configure(bg=preto)
        s_green.configure(bg=preto)
        s_blue.configure(bg=preto)
        dark_mode_button.configure(text="Light Mode")
        dark_mode = True

#cores:
preto = "#181818"
branco = "#feffff"
dark_mode = False

#criando interface:
janela = Tk()
janela.geometry('530x250')
janela.configure(bg=branco)

#configurando a tela principal:
tela = Label(janela, bg=preto, width=40, height=10, bd=1)
tela.grid(row=0, column=0, columnspan=3)

#freme direito:
frame_direita = Frame(janela, bg=branco)
frame_direita.grid(row=1, column=0)

#freme baixo:
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

#botão do modo escuro brabo:
dark_mode_button = Button(janela, text="Modo escuro", command=toggle_dark_mode)
dark_mode_button.grid(row=3, column=0, columnspan=3, pady=10)

#loop da janela:
janela.mainloop()