matriz = []
for i in range(4):
    matriz.append([0]*5)

# matriz [0][1] = '1'
# matriz [0][2] = '2'
# matriz [0][3] = "3"
# matriz [0][4] = "4"
# matriz [0][5] = "5"

num = 1

for lin in range(4):
    for col in range(5):
        matriz[lin][col] = num
        num += 1



for linha in matriz:
    print(linha)

