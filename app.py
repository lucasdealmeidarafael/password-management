from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image
import random
import string

# Cores
co0 = "#444666"
co1 = "#feffff"
co2 = "#6f9fbd"
co3 = "#f05a43"

fundo_dark = "#484f66"
fundo_claro = "#ffffff"

fundo = co1

root = Tk()
root.title("Gerenciamento de Senhas")
root.geometry("300x360")
root.configure(bg=fundo)

# Frames
frame_main = Frame(root, width=300, height=110, bg=fundo,
                   pady=0, padx=0, relief="flat")
frame_main.grid(row=0, column=0)

frame_box = Frame(root, width=300, height=220, bg=fundo,
                  pady=0, padx=0, relief="flat")
frame_box.grid(row=1, column=0)

style = ttk.Style(root)
style.theme_use("clam")

img_0 = Image.open("password.png")
img_0 = img_0.resize((30, 30), Image.ANTIALIAS)
img_0 = ImageTk.PhotoImage(img_0)

app_imagem = Label(frame_main, height=60, image=img_0,
                   compound=LEFT, padx=10, relief="flat", anchor="nw",
                   font=("Ivy 16 bold"), bg=co1, fg=co3)
app_imagem.place(x=2, y=0)

app_name = Label(frame_main, text="Gerador de Senhas", height=1, width=20,
                 padx=0, relief="flat", anchor="nw",
                 font=("Ivy 16 bold"), bg=co1, fg=co0)
app_name.place(x=35, y=2)

app_linha = Label(frame_main, text="", height=1, width=400,
                  padx=0, relief="flat", anchor="nw",
                  font=("Arial 1"), bg=co3, fg=co1)
app_linha.place(x=0, y=35)

alfabeto_menos = string.ascii_lowercase
alfabeto_mais = string.ascii_uppercase
numeros = "123456789"
simbolos = "[]{}()*;/,_"

var = IntVar()
var.set(8)