# ===== IMPORTACOES =====
import tkinter as tk
from tkinter import messagebox

# ===== VARIAVEIS =====
JANELA_LARGURA = 310
JANELA_ALTURA = 140

# ===== FUNÇÕES =====
def abrir_novo_registro():
    messagebox.showinfo("OPS, EM TRABALHO AINDA", "Essa função ainda estar em obra!")

def abrir_antigos_registro():
    messagebox.showinfo("OPS, EM TRABALHO AINDA", "Essa função ainda estar em obra!")

# ===== Janela
janela = tk.Tk()
janela.title("SOFTWARE DE BALANÇA")

janela.update_idletasks()
posicaox = (janela.winfo_screenwidth() // 2) - (JANELA_LARGURA // 2)
posicaoy = (janela.winfo_screenheight() // 2) - ((JANELA_ALTURA // 2)+30)
janela.geometry(f"{JANELA_LARGURA}x{JANELA_ALTURA}+{posicaox}+{posicaoy}")
janela.resizable(False, False)

# ===== Botões
botao1 = tk.Button(
    janela,
    text="ADICIONAR UM NOVO REGISTRO",
    width=35,
    height=2,
    command=abrir_novo_registro,
    font=("Arial", 10, "bold")
)
botao1.pack(pady=15)

botao2 = tk.Button(
    janela,
    text="VER REGISTROS EXISTENTE",
    width=35,
    height=2,
    command=abrir_antigos_registro,
    font=("Arial", 10, "bold")
)
botao2.pack()

# ===== Loop principal
janela.mainloop()