# 7. Modique o algoritmo de busca simples para retornar a posição de todas as ocorrências de x
# dentro da lista. Note que, o retorno desta função será uma outra lista. Quando o elemento
# x não pertence à lista de busca, o que você vai retornar?



def busca_linear_todas_ocorrencias(lista, x):
    indices = []  # Lista para armazenar os índices das ocorrências de x
    for i in range(len(lista)):
        if lista[i] == x:
            indices.append(i)  # Adiciona o índice à lista se o valor for encontrado
    return indices  # Retorna a lista de índices encontrados

# Definição da lista e valor procurado
lista = [2, 5, 7, 10, 12, 5, 15, 5]
valor_procurado = 5  # Valor que queremos encontrar em todas as suas ocorrências

# Teste da busca linear para todas as ocorrências e impressão direta
indices = busca_linear_todas_ocorrencias(lista, valor_procurado)
print(f"{indices}.")
