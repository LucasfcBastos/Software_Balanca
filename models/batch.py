from models.cattle import Cattle

# ===== CLASSE =====
class Batch:

    # ===== Função Principal
    def __init__(self, bovino):
        self.tipo_bovino = bovino
        self.status = "Pre Iniciado"
        self.lado_b = False
        self.quant = 0
        self.animais = []

    # ===== Função de Registro
    def registrar(self, peso):
        
        # forçar a variavel ser ponto flutuante
        peso = float(peso)

        # condição para criar os animais para registrar seus dados
        if not self.animais or self.lado_b == False:

            # definir o id dele
            novo_id = len(self.animais) + 1

            # criando uma nova classe animal
            cattle = Cattle(novo_id)

            # colocando os dados dentro do animal
            cattle.banda_a = peso
            cattle.total_kg = cattle.banda_a
            cattle.arroba = cattle.total_kg / 15

            # salvando os dados dentro da array
            self.animais.append(cattle)

            # aumentando a quantidade e alterando o boolean
            self.lado_b = True
            self.quant += 0.5

        else:

            # pega o ultimo registro, que não tem a banda b
            cattle = self.animais[-1]

            # salva a banda b e atualizando os dados
            cattle.banda_b = peso
            cattle.total_kg = cattle.banda_a + cattle.banda_b
            cattle.arroba = cattle.total_kg / 15

            # aumentando a quantidade e alterando o boolean
            self.lado_b = False
            self.quant += 0.5
            
        # atualizando o status
        if self.quant != 0:
            self.status = "Em processo"
        
        return