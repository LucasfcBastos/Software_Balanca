# ===== IMPORTAÇÕES =====
import tkinter as tk
import platform
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ===== FUNÇÕES =====
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