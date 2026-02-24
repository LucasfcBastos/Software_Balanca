# ===== IMPORTAÇÕES =====
import json
import os
from datetime import datetime

# ===== VARIAVEIS =====
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ===== FUNÇÕES =====

# ===== Função para puxar os dados do produtor
def carregar_produtor():

    # monta o caminho completo até o arquivo config/produtor.json
    caminho = os.path.join(BASE_DIR, "config", "produtor.json")

    # abre o arquivo para ler e carregar o conteúdo do json
    with open(caminho, "r", encoding="utf-8") as f:
        dados = json.load(f)

    # retorna o primeiro item da lista se existir, ou retorna vazio
    return dados[0] if dados else {}

# ===== Função para puxar os dados da industria
def carregar_industria():

    # monta o caminho completo até o arquivo config/industria.json
    caminho = os.path.join(BASE_DIR, "config", "industria.json")

    # abre o arquivo para ler e carregar o conteúdo do json
    with open(caminho, "r", encoding="utf-8") as f:
        dados = json.load(f)

    # retorna o primeiro item da lista se existir, ou retorna vazio
    return dados[0] if dados else {}

# ===== Função para salvar o abate
def salvar_abate(dados_abate):

    # monta o caminho completo até o arquivo data/abates.json
    caminho = os.path.join(BASE_DIR, "data", "abates.json")

    # se o arquivo ainda não existir, cria ele com uma lista vazia
    if not os.path.exists(caminho):
        with open(caminho, "w", encoding="utf-8") as f:
            json.dump([], f)

    # abre o arquivo para leitura
    with open(caminho, "r", encoding="utf-8") as f:
        try:
            abates = json.load(f)
        except:
            abates = []
    
    # define o id pelo tamanho do json
    novo_id = len(abates)

    # criar mais um dado com informação
    dados_abate["id"] = novo_id + 1

    # pega o dia é hora do momento que foi executado
    agora = datetime.now()

    # criar mais um dado com informação
    dados_abate["data_registro"] = agora.strftime("%d/%m/%Y %H:%M:%S")

    # adiciona esses dados junto ao abate
    abates.append(dados_abate)

    # Abre o arquivo novamente no modo escrita
    with open(caminho, "w", encoding="utf-8") as f:
        # Salva a lista atualizada no arquivo
        json.dump(abates, f, indent=4, ensure_ascii=False)

# ===== Função para salvar o abate
def listar_abate():

    # monta o caminho completo até o arquivo data/abates.json
    caminho = os.path.join(BASE_DIR, "data", "abates.json")

    if not os.path.exists(caminho):
        return []

    with open(caminho, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except:
            return []
