n = int(input("Digite a quantidade de produtos: "))

for _ in range (n):
    atual = int(input("Digite o valor atual: "))
    reajustado = int(input("Digite o valor reajustado: "))

    aumento =  reajustado - atual
    percentual = (reajustado* 100) / atual - 100

    print(f"O aumento em R$: {aumento}")
    print(f"O valor do percentual é de {percentual:.2f}% ")