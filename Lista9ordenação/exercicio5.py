# 5. Implemente a ordenação da bolha como um único método, ou seja, dentro do método haverão
# comandos de repetição encadeados.


def bubble_sort_unico(lista):
    for i in range(len(lista)):
        for j in range(len(lista) - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

# Testando o método de ordenação
lista = [34, 7, 23, 32, 5, 62, 32, 8, 45, 3, 15, 27, 56, 12, 10]
print("Lista antes da ordenação:", lista)
bubble_sort_unico(lista)
print("Lista depois da ordenação:", lista)
