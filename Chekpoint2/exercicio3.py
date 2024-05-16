cedula = int(input("Digite o valor da cédula: "))
moeda1 = int(input("Digite o valor da primeira moeda: "))
moeda2 = int(input("Digite o valor da ssegunda moeda: "))

for i in range(cedula // moeda1 + 1):
    guarda = moeda1 * i
    for j in range(cedula // moeda2 + 1):
        guarda2 = moeda2 * j
        if guarda + guarda2 == cedula:
            print(f"Poss´vel: {i} moeda(s) de {moeda1} e {j} moeda(s) de {moeda2}")
            exit(0)
print("Não foi possivel ")