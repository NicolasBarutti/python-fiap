import Imagem

matrizes = Imagem . getMatrizImagemColorida ("lago_canada.jpg")
matrizR = matrizes [0]
matrizG = matrizes [1]
matrizB = matrizes [2]

for i in range ( len ( matrizR )):
 for j in range ( len ( matrizR [i ]) ):
    matrizR [i ][ j] = matrizR [i ][ j] + 100
    matrizG [i ][ j] = matrizG [i ][ j] + 70
    matrizB [i ][ j] = matrizB [i ][ j] + 70

Imagem . salvaImagemColorida ("lago_canada_claro.jpg",matrizR , matrizG , matrizB )