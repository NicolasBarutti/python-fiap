cpf = int(input("Digite aqui seu CPF: "))



ultimosDoisNumeros = cpf % 100
cpf = cpf // 100


cpf3 = cpf % 1000
cpf = cpf // 1000

cpf2 = cpf % 1000
cpf = cpf // 1000
 



# ultimosDoisNumeros = cpf[-2:len(cpf)]
# cpf = cpf[0:-2]



print(f"{cpf}.{cpf2}.{cpf3}-{ultimosDoisNumeros}")


