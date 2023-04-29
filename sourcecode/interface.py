import os
import time
from tkinter import *
import subprocess
from tkinter import font
import tkinter.messagebox
import platform

bg_color = '#183632'
fg_color = '#F4F4F4' 
button_color = '#387780' 
button_hover_color = '#007E33' 
text_color = '#F4F4F4' 

root = Tk()
root.title("Gerador de Senhas by Inacio Buemo")
root.geometry("400x250")
root.config(bg=bg_color)


font_path = "./urbani.ttf" 
custom_font = font.Font(family="Urbani", size=20, weight="bold")
custom_font['family'] = font.Font(family="Urbani", name='custom_font')

button_style = {
    'font': ('Urbani', 12, 'bold'),
    'fg': fg_color,
    'bg': button_color,
    'activebackground': button_hover_color,
    'activeforeground': fg_color,
    'padx': 10,
    'pady': 5,
    'border': 0,
    'relief': 'flat',
}

label_style = {
    'font': custom_font,
    'fg': text_color,
    'bg': bg_color,
    'pady': 10,
}

lbl_senha = Label(root, text="", **label_style)
lbl_senha.pack()

senhaLabel = Label(root, text="", **label_style)
senhaLabel.pack()

senha_gerada = ""

if (platform.system() == 'Windows' or 'Linux'):
    os.system("g++ geradordesenha.cpp -o ../bin/gerador")
else:
    print("ERRO: SISTEMA OPERACIONAL DESCONHECIDO.")

def gerar_senha():
    global senha_gerada
    senha = subprocess.check_output("../bin/./gerador")
    senha_str = senha.decode().strip()
    lbl_senha.config(text=senha_str)
    senha_gerada = senha_str

def copiar_senha():
    global senha_gerada
    if senha_gerada != "":
        root.clipboard_clear()
        root.clipboard_append(senha_gerada)

def limpar_senha():
    lbl_senha.config(text="")
    senhaLabel.config(text="")
    global senha_gerada
    senha_gerada = ""

def salvar_senha(senha):
    diretorio = os.path.abspath('../senhas_salvas')
    if not os.path.exists(diretorio):
        os.makedirs(diretorio)
    arquivos_salvos = len(os.listdir(diretorio))
    nome_arquivo = f'senha{arquivos_salvos+1}.txt'
    with open(os.path.join(diretorio, nome_arquivo), 'w') as arquivo:
        arquivo.write(senha)
    tkinter.messagebox.showinfo('Senha Salva', f'Senha salva em {os.path.join(diretorio, nome_arquivo)}')
    
def salvar_senha_cpp(senha):
    subprocess.call(["./salvar_senha.exe", senha])

def salvar_em_txt():
    global senha_gerada
    if senha_gerada != "":
        salvar_senha(senha_gerada)
        salvar_senha_cpp(senha_gerada)
        
button_frame = Frame(root, bg=bg_color)
button_frame.pack(expand=True)

button_width = int(root.winfo_width() * 0.4 / 3)

gerarButton = Button(button_frame, text="Gerar Senha", command=gerar_senha, width=button_width, **button_style)
gerarButton.pack(side=LEFT, padx=10, pady=10)

copiarButton = Button(button_frame, text="Copiar Senha", command=copiar_senha, width=button_width, **button_style)
copiarButton.pack(side=LEFT, padx=10, pady=10)

limparButton = Button(root, text="Limpar Senha", command=limpar_senha, width=button_width, **button_style)
limparButton.pack(side=BOTTOM, pady=10)

salvarButton = Button(button_frame, text="Salvar em txt", command=salvar_em_txt, width=button_width, **button_style)
salvarButton.pack(side=LEFT, padx=10, pady=10)

root.mainloop()
