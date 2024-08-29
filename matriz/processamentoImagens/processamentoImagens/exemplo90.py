import Imagem

matriz = Imagem.getMatrizImagemCinza("olhos.jpg")

rat = []

lin = len(matriz)
col = len(matriz[0])



for i in range(lin):
    rat.append([0] * lin)





for i in range(lin):
    for j in range(col):
        rat[j][i] = matriz[j][i]



Imagem.salvaImagemCinza("olhos90.jpg", rat)