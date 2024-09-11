def insertion_sort(lista):
    for i in range(1, len(lista)):
        chave = lista[i]
        j = i - 1
        while j >= 0 and chave < lista[j]:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = chave

def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

def selection_sort(lista):
    for i in range(len(lista)):
        min_idx = i
        for j in range(i+1, len(lista)):
            if lista[j] < lista[min_idx]:
                min_idx = j
        lista[i], lista[min_idx] = lista[min_idx], lista[i]

lista = [1, 65, 2, 1, 3, 5, 6, 2, 1, 2, 3, 45, 3, 21]

# Testando Insertion Sort
lista_insertion = lista.copy()
insertion_sort(lista_insertion)
print("Após Insertion Sort:", lista_insertion)

# Testando Bubble Sort
lista_bubble = lista.copy()
bubble_sort(lista_bubble)
print("Após Bubble Sort:", lista_bubble)

# Testando Selection Sort
lista_selection = lista.copy()
selection_sort(lista_selection)
print("Após Selection Sort:", lista_selection)
