import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def carregar_produtor():
    caminho = os.path.join(BASE_DIR, "config", "produtor.json")

    with open(caminho, "r", encoding="utf-8") as f:
        dados = json.load(f)

    return dados[0] if dados else {}

def carregar_industria():
    caminho = os.path.join(BASE_DIR, "config", "industria.json")

    with open(caminho, "r", encoding="utf-8") as f:
        dados = json.load(f)

    return dados[0] if dados else {}