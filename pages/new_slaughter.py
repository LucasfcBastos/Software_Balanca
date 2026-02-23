# ===== IMPORTACOES =====
from tkinter import messagebox
from components.patterns import *
from components.database import *
from pages.new_batch import NewBatch

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

        # label da borda do abate
        label_abate = criar_label(self.janela, "Abate de Bovinos")

        # container de dado do produtor
        produtor = criar_frame(label_abate)

        dados_produtor = carregar_produtor()

        campo_form(produtor, "Produtor", dados_produtor["Nome"])

        # container de dado da industria
        industria = criar_frame(label_abate)

        dados_industria = carregar_industria()

        campo_form(industria, "Industria", dados_industria["Nome"])

        # botão para adiconar lote
        frame_add_lote = criar_frame(label_abate)

        botao1 = criar_botao(
            frame_add_lote,
            "ADICIONAR LOTE",
            self.adicionar_lote
        )
        botao1.pack(side="right")

        # label da borda do lote
        label_lote = criar_label(label_abate, "Lotes dos Bovinos")

        # tabela dos todos os lotes registrados
        colunas = ("ID", "Tipo de Bovinos", "Status do Lote", "Quant. Abatidos", "Visualizar")

        self.tabela = criar_tabela(label_lote, colunas)

        self.tabela.bind("<Double-1>", self.visualizar_lote)

        # botão para finalizar o abate
        frame_out_abate = criar_frame(label_abate)

        self.botao2 = criar_botao(
            frame_out_abate,
            "FINALIZAR ABATE",
            self.finalizar_abate
        )
    
    def adicionar_lote(self):
        # exibição de mensagem sobre o tipo
        resposta = messagebox.askyesnocancel(
            "Tipo de Bovino no Lote",
            "SIM = BOVINOS FEMEA P/ABATER\nNÃO = BOVINOS MACHO P/ABATER"
        )

        # validação e registro da resposta
        if resposta is True:
            tipo = "BOVINOS FEMEA P/ABATER"
        elif resposta is False:
            tipo = "BOVINOS MACHO P/ABATER"
        else:
            return
        
        self.janela.withdraw()
        NewBatch(self, tipo)
    
    def visualizar_lote(self):
        messagebox.showinfo("OPS, EM TRABALHO AINDA", "Essa função ainda estar em obra!")

    def finalizar_abate(self):
        messagebox.showinfo("OPS, EM TRABALHO AINDA", "Essa função ainda estar em obra!")

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