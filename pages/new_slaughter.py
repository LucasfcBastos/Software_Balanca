# ===== IMPORTACOES =====
from tkinter import messagebox
from components.patterns import *

# ===== VARIAVEIS =====
JANELA_LARGURA = 900
JANELA_ALTURA = 500

# ===== CLASSE =====
class NewSlaughter:

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
        
        # mensagem de confimação para fechar
        confirmar = messagebox.askyesno(
            "Cancelar Abate",
            "Deseja realmente cancelar o abate?"
        )

        # se realmente deseja fecha, volta pra tela anterior
        if confirmar:
            self.janela.destroy()
            self.parent.deiconify()