# ===== IMPORTACOES =====
from tkinter import messagebox
from components.patterns import *

# ===== VARIAVEIS =====
JANELA_LARGURA = 310
JANELA_ALTURA = 140

# ===== FUNÇÕES =====
def abrir_novo_registro():
    messagebox.showinfo("OPS, EM TRABALHO AINDA", "Essa função ainda estar em obra!")

def abrir_antigos_registro():
    messagebox.showinfo("OPS, EM TRABALHO AINDA", "Essa função ainda estar em obra!")

# ===== Janela
janela = criar_janela(
    JANELA_LARGURA,
    JANELA_ALTURA
)

# ===== Botões
botao1 = criar_botao(
    janela,
    "ADICIONAR UM NOVO REGISTRO",
    abrir_novo_registro
)
botao1.pack(pady=15)

botao2 = criar_botao(
    janela,
    "VER REGISTROS EXISTENTE",
    abrir_antigos_registro
)

# ===== Loop principal
janela.mainloop()