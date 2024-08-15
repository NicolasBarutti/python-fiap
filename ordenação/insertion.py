# exemplo de mudar apenas um numero para ordenar a lista

# def organiza(lista : list):
#     pos = len(lista) - 1
#     aux = lista[pos]
#     while pos > 0 and lista[pos-1] > aux:
#         lista[pos] = lista[pos-1]
#         pos = pos - 1
#     lista[pos] = aux

    


# if __name__ == '__main__':
#     conj= [5, 7, 11, 14, 25, 13]
#     organiza(conj)
#     print(conj)

def organiza(lista: list, pos: int):
    aux = lista[pos]
    
    while pos > 0 and lista[pos-1] > aux:
        lista[pos] = lista[pos-1]
        pos = pos - 1
    lista[pos] = aux

def insertion_sort(lista : list):
    for i in range(1, len(lista)):
        organiza(lista, i)

    


if __name__ == '__main__':
    conj = [2, 7, 1, 21, 14, 89, 100, 101, 12, 11, 22, 11, 123, 1321, 500, 909]
    insertion_sort(conj)
    print(conj)