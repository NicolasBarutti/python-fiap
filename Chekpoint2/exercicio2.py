# n = int(input("Quantidade de Produtos:"))

# maior_aumento = 0
# maiorPercentual = 0


# atual = int(input("Digite o valor de produtos: "))
# reajustado = int(input("Digite o valor de produtos: "))

# aumento = atual - reajustado
# percentual = (aumento / reajustado) * 100

# if aumento > maior_aumento:
#     maior_aumento = aumento

# if percentual > maiorPercentual:
#     maiorPercentual = percentual

# print(f"O aumento em R$ foi de {maior_aumento}")
# print(f"O aumento percentual foi de { maiorPercentual}%")


n = int(input("Digite a quantidade de produtos: "))


atual = int(input("Digite o valor atual: "))
reajustado = int(input("Digite o valor reajustado: "))

aumento = atual - reajustado
percentual = (aumento / reajustado) * 100

print(f"O aumento em R$: {aumento}")
print(f"O valor do percentual é de {percentual}%")