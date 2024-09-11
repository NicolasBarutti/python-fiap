#  Simule o algoritmo busca simples e o busca binária quando os itens procurados não pertencem
# ao vetor.


def busca_binaria(vet, x):
    inicio = 0
    fim = len(vet) - 1
    while inicio <= fim:
        meio = (inicio + fim) // 2
        if vet[meio] > x:
            fim = meio - 1
        elif vet[meio] < x:
            inicio = meio + 1
        else:
            return meio
    return -1

def busca_linear(vetor, valor):
    for i in range(len(vetor)):
        if vetor[i] == valor:
            return i  # Retorna o índice se encontrado
    return -1  # Retorna -1 se não encontrado

# Exemplo de uso
vetor = [2, 5, 7, 10, 12, 15]
valor_procurado = 8  # Valor não presente no vetor

# Teste da busca linear
indice_linear = busca_linear(vetor, valor_procurado)
if indice_linear != -1:
    print(f"Busca Linear: Elemento {valor_procurado} encontrado no índice {indice_linear}.")
else:
    print(f"Busca Linear: Elemento {valor_procurado} não encontrado no vetor.")

# Teste da busca binária
indice_binario = busca_binaria(vetor, valor_procurado)
if indice_binario != -1:
    print(f"Busca Binária: Elemento {valor_procurado} encontrado no índice {indice_binario}.")
else:
    print(f"Busca Binária: Elemento {valor_procurado} não encontrado no vetor.")

