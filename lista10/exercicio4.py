# 4 soma das posições

def somaPos(matriz):
    soma = 0
    for linha in matriz:
        for valor in linha:
            if valor > 0:
                soma += valor
    return soma

# Exemplo de uso
matriz_exemplo = [[1, -2, 3], [-4, 5, 6]]
print(somaPos(matriz_exemplo))  # Saída: 15
