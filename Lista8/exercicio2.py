# 2. Escreva um programa que faz uso das funções de busca implementados nos eslaides.



# Função de busca simples (linear)
def busca_linear(vetor, valor):
    posicoes = []
    for i in range(len(vetor)):
        if vetor[i] == valor:
            return i
    return - 1
    

# Função de busca binária
def busca_binaria(vetor, valor):
    inicio = 0
    fim = len(vetor) - 1
    posicoes = []
    
    # Busca binária simples
    while inicio <= fim:
        meio = (inicio + fim) // 2
        if vetor[meio] == valor:
            posicoes.append(meio)  # Encontra uma ocorrência
            # Checa por outras ocorrências à esquerda e à direita do meio
            i = meio - 1
            while i >= 0 and vetor[i] == valor:
                posicoes.append(i)
                i -= 1
            i = meio + 1
            while i < len(vetor) and vetor[i] == valor:
                posicoes.append(i)
                i += 1
            return sorted(posicoes)  # Retorna todas as ocorrências em ordem
        elif vetor[meio] > valor:
            fim = meio - 1
        else:
            inicio = meio + 1
    
    return [-1]  # Retorna -1 se não encontrado

# Função principal para testar as buscas
def main():
    vetor = [2, 5, 7, 10, 12, 15, 15, 15, 18, 20]
    valor_procurado = 15

    print(f"Vetor: {vetor}")
    print(f"Valor procurado: {valor_procurado}")

    # Busca linear
    posicoes_linear = busca_linear(vetor, valor_procurado)
    print(f"Busca Linear - Posições: {posicoes_linear}")

    # Busca binária (o vetor já está ordenado)
    posicoes_binaria = busca_binaria(vetor, valor_procurado)
    print(f"Busca Binária - Posições: {posicoes_binaria}")

# Chama a função principal
if __name__ == "__main__":
    main()
