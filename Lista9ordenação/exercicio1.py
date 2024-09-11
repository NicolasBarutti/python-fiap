


def lista_ordenada(lista):
    # Verifica se o elemento no índice i é menor ou igual ao próximo elemento
    for i in range(len(lista) - 1):  # O loop vai até o penúltimo elemento
        if lista[i] > lista[i + 1]:
            return False  # A lista não está ordenada
    return True  # A lista está ordenada

# Exemplo de uso
lista1 = [1.2, 2.5, 3.8, 4.0, 5.5]
lista2 = [1.2, 3.5, 2.8, 4.0, 5.5]

print(f"Lista 1 está ordenada? {lista_ordenada(lista1)}")
print(f"Lista 2 está ordenada? {lista_ordenada(lista2)}")
