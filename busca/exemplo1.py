def busca (conjunto: list, valor: float) -> int :
    i = 0
    while i < len (conjunto) and conjunto [i] != valor:
        i = i + 1
    if i == len (conjunto) :
        return -1
    else :
        return i
    
lista = [-5.5, 0.9, 3.6, 7.2, 2.2, 1.1, 6.6, 8.9,]
x = 3.6
resp = busca(lista, x)
print(f"o valor {x} está na posição {resp} da lista")