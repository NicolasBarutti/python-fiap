# Escreva uma função que elimina elementos repetidos de uma lista. Sua função recebe uma
# lista A contendo ou não valores repetidos e retorna uma outra lista contendo todos os
# elementos de A sem repetição.



def remove_repetidos(lista):
    lista_sem_repetidos = []
    for item in lista:
        if item not in lista_sem_repetidos:
            lista_sem_repetidos.append(item)
    return lista_sem_repetidos

# Exemplo de uso
lista_original = [1, 2, 2, 3, 4, 4, 5]
lista_sem_repetidos = remove_repetidos(lista_original)
print("Lista original:", lista_original)
print("Lista sem repetidos:", lista_sem_repetidos)
