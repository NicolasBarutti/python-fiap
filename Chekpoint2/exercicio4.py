n = int(input("Digite o número de elementos na sequência: "))

soma = 0
quantidade = 0
contagem = 0

while contagem < n:
    numero = float(input("Digite o {}º número da sequência: "))
    if numero > 50:
        soma = soma + numero
    if numero < 100:
        quantidade = quantidade + 1
    contagem = contagem + 1

print("A somatória dos números maiores que 50 é:", soma)
print("A quantidade de números menores que 100 é:", quantidade)