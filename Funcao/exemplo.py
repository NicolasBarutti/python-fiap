def aumento (valor , percentual):
    valor = valor + valor * percentual / 100
    return valor

def divisao_resto(a, b):
    return (a // b, a % b)

vl = 1000
perc = 25

aux = aumento(vl, perc)
print(aux)

aux = aumento(400_000, 0.5)
print(aux)

aux = divisao_resto (32, 4)
print(aux)