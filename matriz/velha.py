matriz = []

def criaJogo(matriz):
    for i in range(3):
        matriz.append([' ']*3)

criaJogo(matriz)

def temEspaco ( matriz ):
    for linha in matriz:
        if " " in linha:
            return True
        return False
       
temEspaco(matriz)







for linha in matriz:
    print(linha)