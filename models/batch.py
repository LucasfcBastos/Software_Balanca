# ===== CLASSE =====
class Batch:

    # ===== Função Principal
    def __init__(self, bovino):
        self.tipo_bovino = bovino
        self.status = "Pre Iniciado"
        self.lado_b = False
        self.animais = []