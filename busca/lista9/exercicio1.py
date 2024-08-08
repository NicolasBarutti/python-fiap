#  Simule o algoritmo busca simples e o busca binária quando os itens procurados não pertencem
# ao vetor.

def buscaSimples(vet, x):
    i = 0
    for i in range(len(vet)):
        if vet[i] == x:
            return i
    return -1

vet = [ 1,2,3,4,5,6,7,8,9]
resp = buscaSimples(vet,1)
print(resp)

def buscaBinaria(vet2, x):
    ini = 0
    fim = len(vet2) - 1
    while ini <= fim:
        meio = (ini + fim) // 2
        if vet [ meio ] > x :
            fim = meio - 1
        elif vet [ meio ] < x:
            ini = meio + 1
        else :
            return meio
    return -1

vet2= [2,3,4,6,7,9,12,13,15]
resp2 = buscaBinaria(vet2, 2)
print(resp2)