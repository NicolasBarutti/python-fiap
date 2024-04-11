cpf = int(input("Informe o cpf: "))
soma = 0
multi = 2

while cpf > 999_999_999:
    cpf = int(input("Inválido"))

while cpf != 0:
    dig = cpf % 10
    soma = soma + dig * multi
    cpf = cpf // 10
    multi = multi + 1

resto = soma % 11
if resto < 2:
    print("Primeiro digito: 0")
else:
    print(f"primeiro digito: {11-resto}")
