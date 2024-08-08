#  Escreva uma função que elimina elementos repetidos de uma lista. Sua função recebe uma
# lista A contendo ou não valores repetidos e retorna uma outra lista contendo todos os
# elementos de A sem repetição.

def eliminaNumero(vet):
    novoVetor = []
    for i in vet:
        if i not in novoVetor:
            novoVetor.append(i)
    return novoVetor


vet = [1, 2, 3, 4, 5, 6, 6, 7, 7, 8]


resultado = eliminaNumero(vet)
print(resultado)
