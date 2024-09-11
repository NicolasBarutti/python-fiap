# 1. Crie a matriz do jogo da velha abaixo e faça a impressão na tela:



def imprimir_matriz(matriz):
    for linha in matriz:
        print(" ".join(linha))

matriz_jogo_da_velha = [
    ["x", "o", "x"],
    ["o", "x", " "],
    ["o", "x", " "]
]

imprimir_matriz(matriz_jogo_da_velha)
