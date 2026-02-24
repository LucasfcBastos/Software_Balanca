# ===== IMPORTACOES =====
from tkinter import messagebox
from components.patterns import *
from components.database import *
from pages.new_batch import NewBatch
from models.slaughter import Slaughter
from models.batch import Batch

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

        # instanciando a classe abate
        self.abate = Slaughter()

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
        
        # instanciando a classe lote
        novo_lote = Batch(tipo)

        # abrir a nova tela
        self.janela.withdraw()
        NewBatch(self, self.abate, novo_lote)
    
    # ===== Função para atualizar a tabela de dados
    def atualizar_tabela(self):

        # remove todos os itens atuais da tabela
        for item in self.tabela.get_children():
            self.tabela.delete(item)

        # percorre todos os lotes cadastados
        for index, lote in enumerate(self.abate.lotes, start=1):

            # se o estatus do lote for finalizado, exibe:
            if lote.status == "Lote Finalizado":

                # insere uma nova linha na tabela
                self.tabela.insert(
                    # item pai, insere no final e valores que aparecem
                    "",
                    "end",
                    values=(
                        index,
                        lote.tipo_bovino,
                        lote.status,
                        lote.quant,
                        "Não permitido"
                    )
                )
            else:

                # insere uma nova linha na tabela
                self.tabela.insert(
                    # item pai, insere no final e valores que aparecem
                    "",
                    "end",
                    values=(
                        index,
                        lote.tipo_bovino,
                        lote.status,
                        lote.quant,
                        "Permitido"
                    )
                )

    # ===== Função visualizar lote selecionado
    def visualizar_lote(self, event):
    
        # ele registrar o que foi selecionado
        selecionado = self.tabela.selection()
        
        # validar se realmente foi selecionado algo
        if not selecionado:
            return

        # pega o primeiro item da lista
        item = selecionado[0]

        # pega todos os valores das colunas
        valores = self.tabela.item(item, "values")

        # pega a informação da ultima coluna
        coluna_visualizar = valores[4]

        # valida se a ultima coluna não possue escrito "Permitido"
        if coluna_visualizar != "Permitido":
            messagebox.showwarning(
                "Aviso",
                "Este lote já foi finalizado e não pode ser visualizado."
            )
            return

        # obtém o indice da linha selecionada
        index = self.tabela.index(item)

        # acessa o lote correspondente ao indice
        lote = self.abate.lotes[index]

        # abrir a nova tela
        self.janela.withdraw()
        NewBatch(self, self.abate, lote)

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