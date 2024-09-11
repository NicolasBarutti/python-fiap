import random

def gerar_matriz_aleatoria(linhas, colunas, intervalo):
    return [[random.randint(0, intervalo) for _ in range(colunas)] for _ in range(linhas)]

matriz_5x7 = gerar_matriz_aleatoria(5, 7, 1000)

# Impressão da matriz para verificação
for linha in matriz_5x7:
    print(linha)
