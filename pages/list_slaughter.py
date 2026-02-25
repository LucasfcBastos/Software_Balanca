# ===== IMPORTACOES =====
from tkinter import messagebox
from components.patterns import *
from components.database import *
from components.export import *

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
        
        if len(abates) > 3:
            container = criar_frame(self.janela)
            container.pack(fill="both", expand=True)

            canvas = tk.Canvas(container)
            scrollbar = tk.Scrollbar(container, orient="vertical", command=canvas.yview)

            scroll_frame = criar_frame(canvas)

            scroll_frame.bind(
                "<Configure>",
                lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
            )

            canvas.create_window((0, 0), window=scroll_frame, anchor="nw")
            canvas.configure(yscrollcommand=scrollbar.set)

            canvas.pack(side="left", fill="both", expand=True)
            scrollbar.pack(side="right", fill="y")
        
        for abate in reversed(abates):

            if len(abates) > 3:
                frame_card = tk.Frame(scroll_frame, bd=2, relief="ridge", padx=10, pady=10)
            else:
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
                lambda id_abate=abate["id"]: self.baixar_pdf(id_abate)
            )
            botao2.pack(side="left", pady=10)

    def baixar_pdf(self, id_abate):
        caminho = gerar_pdf_abate(id_abate)

        if caminho:
            messagebox.showinfo("PDF Gerado", f"PDF salvo em:\n{caminho}")
        else:
            messagebox.showerror("Erro", "Não foi possível gerar o PDF.")

    # ===== Função para fehcar
    def fechar(self):

        # svolta pra tela anterior
        self.janela.destroy()
        self.parent.deiconify()