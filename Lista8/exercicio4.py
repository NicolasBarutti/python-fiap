# 4. Dados uma lista de números inteiros e um inteiro x, escreva um algoritmo que verica se
# existem 2 elementos do conjunto cuja soma seja igual a x. Por exemplo: dado x = 11 e a
# lista abaixo:
# 1 lista = [2, 5, -7, 9, 3, 10, 15, 6]
# seu algoritmo deverá imprimir 2 e 9 ou 5 e 6


def somanumero(lista, x):
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] + lista[j] == x:
                print((f"{lista[i]} e {lista[j]} somam {x}"))


lista = [2, 5, -7, 9, 3, 10, 15, 6]
x = 11
somanumero(lista,x)