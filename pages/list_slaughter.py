# ===== IMPORTACOES =====
from tkinter import messagebox
from components.patterns import *
from components.database import *

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

        # puxar a função exibir a lista
        self.exibir_lista()

    # ===== Função para exibir os abate
    def exibir_lista(self):

        abates = listar_abate()

        if not abates:
            frame_input = criar_frame(self.janela)

            texto = criar_texto(frame_input, "Nenhum registro de abate foi encontrado")
            texto.pack(pady=15)
            return
        
        for abate in reversed(abates):

            frame_card = tk.Frame(self.janela, bd=2, relief="ridge", padx=10, pady=10)
            frame_card.pack(fill="x", padx=10, pady=10)

            frame_produtor = criar_frame(frame_card)
            campo_form(frame_produtor, "Produtor", abate.get('produtor', {}).get('nome', ''))

            frame_industria = criar_frame(frame_card)
            campo_form(frame_industria, "Industria", abate.get('industria', {}).get('nome', ''))

            frame_data = criar_frame(frame_card)
            campo_form(frame_data, "Data", abate.get('data_registro', ''))

            frame_botão = criar_frame(frame_card)
            
            botao2 = criar_botao(
                frame_botão,
                "BAIXAR PDF",
                self.baixar_pdf
            )
            botao2.pack(side="left", pady=10)

    def baixar_pdf(self):
        messagebox.showinfo("OPS, EM TRABALHO AINDA", "Essa função ainda estar em obra!")

    # ===== Função para fehcar
    def fechar(self):

        # svolta pra tela anterior
        self.janela.destroy()
        self.parent.deiconify()