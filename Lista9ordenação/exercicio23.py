# 2. Escolha um dos três algoritmos vistos e faça uma simulação usando uma lista com 15 elementos.

def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

# Lista de exemplo com 15 elementos
lista = [34, 7, 23, 32, 5, 62, 32, 8, 45, 3, 15, 27, 56, 12, 10]

print("Lista antes da ordenação:", lista)
bubble_sort(lista)
print("Lista depois da ordenação:", lista)

# 3 Qual mudança devemos fazer para ordenar as listas em ordem decrescente?

def bubble_sort_descendente(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] < lista[j + 1]:  # Mudança para ordem decrescente
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

# Testando a ordenação em ordem decrescente
lista = [34, 7, 23, 32, 5, 62, 32, 8, 45, 3, 15, 27, 56, 12, 10]
print("Lista antes da ordenação decrescente:", lista)
bubble_sort_descendente(lista)
print("Lista depois da ordenação decrescente:", lista)
