# 1

def busca_simples(vetor, item):
    for i in range(len(vetor)):
        if vetor[i] == item:
            return i
    return -1

vetor = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
item_procurado = 5

print("Resultado da busca simples:", busca_simples(vetor, item_procurado))