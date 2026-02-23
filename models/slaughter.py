# ===== IMPORTACOES =====
from components.database import *

# ===== CLASSE =====
class Slaughter:

    # ===== Função Principal
    def __init__(self):

        dados_produtor = carregar_produtor()
        dados_industria = carregar_industria()

        self.produtor_nome = dados_produtor["Nome"]
        self.produtor_nome = dados_industria["Nome"]
        self.quantidade_lote = 0
        self.lotes = []