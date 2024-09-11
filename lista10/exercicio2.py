# 2. Escreva uma função getDimensao que recebe como parâmetro uma matriz mat de números
# reais (double) e retorna uma tupla (ou uma lista) de inteiros contendo o número de linhas e
# o número de colunas de mat. Note que, sua tupla terá duas posições
def getDimensao(mat):
    # Conta o número de linhas
    num_linhas = len(mat)
    
    # Conta o número de colunas na primeira linha, se a matriz não estiver vazia
    num_colunas = len(mat[0]) if mat else 0
    
    return (num_linhas, num_colunas)

# Exemplo de uso
matriz_exemplo = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

dimensao = getDimensao(matriz_exemplo)
print(dimensao)  # Saída: (3, 3)
