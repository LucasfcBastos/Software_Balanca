# ===== IMPORTACOES =====
from tkinter import messagebox
from components.patterns import *
from pages.new_slaughter import NewSlaughter
from pages.list_slaughter import ListSlaughter

# ===== VARIAVEIS =====
JANELA_LARGURA = 310
JANELA_ALTURA = 140

# ===== FUNÇÕES =====
def abrir_novo_registro():
    janela.withdraw()
    NewSlaughter(janela)

def abrir_antigos_registro():
    janela.withdraw()
    ListSlaughter(janela)

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