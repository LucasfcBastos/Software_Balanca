# ===== IMPORTACOES =====
from tkinter import messagebox
from components.patterns import *

# ===== VARIAVEIS =====
JANELA_LARGURA = 500
JANELA_ALTURA = 650

# ===== CLASSE =====
class ListSlaughter:

    # ===== Função Principal
    def __init__(self, parent):
        
        # guardando objeto na instancia
        self.parent = parent
        
        # janela
        self.janela = criar_janela(
            JANELA_LARGURA,
            JANELA_ALTURA,
            parent=parent
        )
        self.janela.protocol("WM_DELETE_WINDOW", self.fechar)

    # ===== Função para fehcar
    def fechar(self):

        # svolta pra tela anterior
        self.janela.destroy()
        self.parent.deiconify()