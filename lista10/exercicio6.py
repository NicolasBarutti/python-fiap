# 6. Escreva um função busca que recebe como parâmetro uma matriz mat de números reais
# e um real x, sua função deverá retornar a posição (linha e coluna) de x em mat ou a
# lista[-1, -1] caso x não pertença a mat. Note que o retorno deverá ser uma lista de
# inteiros com dois valores, primeiro a linha e depois a coluna.


def busca(matriz, x):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == x:
                return [i, j]
    return [-1, -1]

# Exemplo de uso
matriz_exemplo = [[1, 2], [3, 4]]
valor_procurado = 3
print(busca(matriz_exemplo, valor_procurado))  # Saída: [1, 0]
