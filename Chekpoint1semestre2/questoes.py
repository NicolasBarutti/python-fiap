matriz = [
    ['6','lapis de cor','02','36','16.84'],
    ['13','caderno','13','26','6.58'],
    ['3','compasso','09','32','6.49'],
    ['7','giz de cera','17','39', '4.25'],
    ['13','caderno','13','56','6.28'],
    ['6','lapis de cor','05', '17','16.84'],
    ['4','esquadro','05','57','1.52'],
    ['7','giz de cera','23','13','4.25'],
    ['4','esquadro','25','30','1.52'],
    ['3','compasso','14','12','6.49']
]


for i in range(len(matriz) - 1):
    print(matriz[i])


# exercicio 2 
def maiorFaturamento (matriz ):
    produtoMaior = ""
    maiorFaturamento = 0

    for i in matriz:
        produto = i[1]
        quantidade = int(i[3])

        valorUnitario = float(i[4])

        faturamento = quantidade * valorUnitario

        if faturamento = maiorFaturamento:
            maiorFaturamento = faturamento
            
produtoMaior = produto

print(produtoMaior, maiorFaturamento)
produtoMaior(matriz)
# exercicio 3

def soma(produtoNome , matriz):
    vendas = 0 

    for i in matriz:
        produto = i[1]
        quantidade = int(i[3])

        if produto == produtoNome:
            vendas += quantidade
    return vendas


produto = 'compasso'
quantidadeTotal = soma(produto,matriz)
print(f"O produto {produto} teve um total de vendas{quantidadeTotal}")

    


        







