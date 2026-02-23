# ===== IMPORTAÇÕES =====
import tkinter as tk
from tkinter import ttk
import platform
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ===== FUNÇÕES =====

# Função para criar uma janela
def criar_janela(largura, altura, parent=None):
    if parent:
        janela = tk.Toplevel(parent)
    else:
        janela = tk.Tk()

    sistema = platform.system()

    janela.title("SOFTWARE DE BALANÇA")
    janela.update_idletasks()
    posicaox = (janela.winfo_screenwidth() // 2) - (largura // 2)
    posicaoy = (janela.winfo_screenheight() // 2) - ((altura // 2)+30)
    janela.geometry(f"{largura}x{altura}+{posicaox}+{posicaoy}")
    janela.resizable(False, False)

    caminho_icone = os.path.join(BASE_DIR, "img", "icon.png")

    if sistema == "Windows":
        janela.iconbitmap(caminho_icone)
    else:
        icon = tk.PhotoImage(file=caminho_icone)
        janela.iconphoto(True, icon)

    return janela

# Função para criar uma botão
def criar_botao(parent, texto, funcao):
    botao = tk.Button(
        parent,
        text=texto,
        width=35,
        height=2,
        command=funcao,
        font=("Arial", 10, "bold")
    )
    botao.pack()

    return botao

# Função para criar borda em volta
def criar_label(parent, texto):
    label = tk.LabelFrame(
        parent,
        text=texto,
        padx=10,
        pady=10,
        font=("Arial", 12)
    )
    label.pack(padx=10, pady=10, fill="both", expand=True)

    return label

# Função para criar uma container
def criar_frame(parent):
    frame = tk.Frame(parent)
    frame.pack(fill="x")

    return frame

# Função para criar texto assim | dado: informação |
def campo_form(parent, dado, informacao):
    col_produtor = tk.Label(
        parent,
        text=f'{dado}: ',
        font=("Arial", 12)
    )
    col_produtor.pack(side="left")
    
    cel_produtor = tk.Label(
        parent,
        text=informacao,
        font=("Arial", 12, "bold")
    )
    cel_produtor.pack(side="left")

# Função para criar tabelas de dados
def criar_tabela(parent, dados):
    tabela = ttk.Treeview(
        parent,
        columns=dados,
        show="headings"
    )

    for col in dados:
            tabela.heading(col, text=col)
            tabela.column(col, width=120, anchor="center")

    tabela.pack(fill="both", expand=True)

    return tabela