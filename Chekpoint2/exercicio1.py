quantidade = int(input("Digite o quantos numeros da sequencia: ")) 

guarda = ""
numero_antigo = ""
contador = 0

for i in range(quantidade):
    novo_numero = input("digite um número: ")
    guarda = guarda + (novo_numero + " ")
    if numero_antigo != novo_numero:
        contador += 1
    numero_antigo = novo_numero

print(guarda)
print(contador)