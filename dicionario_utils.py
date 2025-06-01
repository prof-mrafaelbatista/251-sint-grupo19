# dicionario_utils.py
import os

CAMINHO_ARQUIVO = 'dicionario.txt'

def carregar_termos():
    termos = {}
    if os.path.exists(CAMINHO_ARQUIVO):
        with open(CAMINHO_ARQUIVO, 'r', encoding='utf-8') as f:
            for linha in f:
                if ':' in linha:

                    termo, definicao = linha.strip().split(':', 1)
                    termos[termo.strip()] = definicao.strip()
    return termos

def salvar_termos(termos):
    with open(CAMINHO_ARQUIVO, 'w', encoding='utf-8') as f:
        for termo, definicao in termos.items():
            f.write(f"{termo}:{definicao}\n")
