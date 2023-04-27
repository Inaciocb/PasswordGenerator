import os
import pyperclip
import time
from tkinter import *
import subprocess
from tkinter import font
import platform

# definir paleta de cores
bg_color = '#183632' # verde escuro
fg_color = '#F4F4F4' # cinza claro
button_color = '#387780' # verde
button_hover_color = '#007E33' # verde mais escuro
text_color = '#F4F4F4' 

root = Tk()
root.title("Gerador de Senhas")
root.geometry("400x250")
root.config(bg=bg_color)


font_path = "./urbani.ttf" # caminho do arquivo da fonte
custom_font = font.Font(family="Urbani", size=20, weight="bold")
custom_font['family'] = font.Font(family="Urbani", name='custom_font')


# definir estilo dos botões
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

# definir estilo das labels
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

def gerar_senha():
    global senha_gerada

    if (platform.system() == 'Windows'):
        senha = subprocess.check_output("../bin/./gerador.exe")
    elif(platform.system() == 'Linux'):
        os.system("g++ gerador de senha -o ../bin/geradordesenha") 
        senha = subprocess.check_output("./geradordesenha")
    else:
        print("ERRO: SISTEMA OPERACIONAL DESCONHECIDO.")
    
    senha_str = senha.decode().strip()
    lbl_senha.config(text=senha_str)
    senha_gerada = senha_str

def copiar_senha():
    global senha_gerada
    if senha_gerada != "":
        pyperclip.copy(senha_gerada)

def limpar_senha():
    lbl_senha.config(text="")
    senhaLabel.config(text="")
    global senha_gerada
    senha_gerada = ""
    pyperclip.copy("")

def salvar_senha(senha):
    # Verifica se o diretório 'senhas_salvas' existe, se não existir, cria
    if not os.path.exists('senhas_salvas'):
        os.makedirs('senhas_salvas')
    # Cria o nome do arquivo com base na quantidade de arquivos já existentes
    arquivos_salvos = len(os.listdir('senhas_salvas'))
    nome_arquivo = f'senha{arquivos_salvos+1}.txt'
    # Escreve a senha gerada no arquivo
    with open(f'senhas_salvas/{nome_arquivo}', 'w') as arquivo:
        arquivo.write(senha)
    # Exibe uma mensagem para o usuário
    messagebox.showinfo('Senha Salva', f'Senha salva em senhas_salvas/{nome_arquivo}')

def salvar_senha_cpp(senha):
    subprocess.call(["./salvar_senha.exe", senha])

def salvar_em_txt():
    global senha_gerada
    if senha_gerada != "":
        salvar_senha(senha_gerada)
        salvar_senha_cpp(senha_gerada)



# criar os botões
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
