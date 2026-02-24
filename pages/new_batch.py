# ===== IMPORTACOES =====
from tkinter import messagebox 
from components.patterns import *

# ===== VARIAVEIS =====
JANELA_LARGURA = 900
JANELA_ALTURA = 500

# ===== CLASSE =====
class NewBatch:

    # ===== Função Principal
    def __init__(self, parent, abate, lote):
        
        # guardando objeto na instancia
        self.parent = parent
        self.abate = abate
        self.lote = lote
        
        # janela
        self.janela = criar_janela(
                JANELA_LARGURA,
                JANELA_ALTURA,
                parent=parent.janela
        )
        self.janela.protocol("WM_DELETE_WINDOW", self.fechar)

        # label da borda do lote
        label_lote = criar_label(self.janela, "Lote dos Bovinos")

        # container com a informação do tipo de bovino
        frame_texto = criar_frame(label_lote)

        titulo = criar_titulo(frame_texto, self.lote.tipo_bovino)
        titulo.pack(side="left")

        # container com o texto é input para registrar
        frame_input = criar_frame(label_lote)

        texto = criar_texto(frame_input, "Digita o valor do peso: ")
        texto.pack(side="left")

        self.input = criar_input(frame_input, self.adicionar_peso)

        # label de dados do bovinos
        label_bov = criar_label(label_lote, "Dados do Abate")

        # tabela dos todos os lotes registrados
        colunas = ("ID", "Banda A", "Banda B", "Total KG", "Arrobas")

        self.tabela = criar_tabela(label_bov, colunas)

        # container com botão para salvar ou finalizar o lote
        frame_botoes = criar_frame(label_lote)

        botoao1 = criar_botao(
            frame_botoes,
            "VOLTAR E SALVAR",
            self.voltar_salvar
        )
        botoao1.pack(side="left", padx=5)

        botoao2 = criar_botao(
            frame_botoes,
            "FINALIZAR LOTE",
            self.finalizar_lote
        )
        botoao2.pack(side="right", padx=5)

    # ===== Função para adicionar um novo peso
    def adicionar_peso(self, event):
        
        # tenta converter o valor digitado para floar
        try:
            peso = float(self.input.get())

        # caso o valor não seja numérico, gera error
        except ValueError:
            messagebox.showerror("Erro", "Digite um número válido.")
            return
    
        # registrar o peso no lote
        self.lote.registrar(peso)

        # limpa o input após registrar o peso
        self.input.delete(0, "end")

        # chama a função para atualizar a tabela
        self.atualizar_tabela()

    # ===== Função para atualizar a tabela de dados
    def atualizar_tabela(self):

        # remove todos os itens atuais da tabela
        for item in self.tabela.get_children():
            self.tabela.delete(item)

        # percorre todos os animais cadastados
        for animal in self.lote.animais:

            #insere uma nova linha na tabela
            self.tabela.insert(
                # item pai, insere no final e valores que aparecem
                "",
                "end",
                values=(
                animal.id,
                f"{animal.banda_a:.2f}",
                f"{animal.banda_b:.2f}",
                f"{animal.total_kg:.2f}",
                f"{animal.arroba:.2f}"
                )
            )

    # ===== Função para salvar o lote
    def voltar_salvar(self):
        messagebox.showinfo("OPS, EM TRABALHO AINDA", "Essa função ainda estar em obra!")

    # ===== Função para finalizar o lote
    def finalizar_lote(self):
        messagebox.showinfo("OPS, EM TRABALHO AINDA", "Essa função ainda estar em obra!")
      
    # ===== Função para fehcar
    def fechar(self):

        # mensagem de confimação para fechar
        confirmar = messagebox.askyesno(
            "Cancelar Lote",
            "Deseja realmente cancelar o lote?"
        )

        # se realmente deseja fecha, volta pra tela anterior
        if confirmar:
            self.janela.destroy()
            self.parent.janela.deiconify()