#exercicio 1

# num = float(input("Digite o numero:"))

# if  num > 10:
#     print(num, "seu numero é maior que 10")
# else:
#     print(num)

# exercico 2 

# num_A = float(input("digite o primeiro numero:"))
# num_B = float(input("digite o segundo numero:"))

# if num_A > num_B:
#     print(num_A,"É maior que o segundo numero")
# elif num_A < num_B:
#     print(num_B, "É maior que o primeiro numero")
# else:
#     print(num_A, "iguais" ,num_B) 

#exercico 4
# timeA = input("Qual é o nome do time: ")
# timeB = input("Qual é o nome do segundo time: ")
# golsA = float(input("QUantos gols o primeiro time fez ? "))
# golsB = float(input("Quantos gols fez o segundo time? "))

# if golsA > golsB:
#     print(f"{timeA} ganhou")
# elif golsA < golsB:
#     print(f"{timeB} ganhou")
# else:
#     print("Empate")        

# exercicio 5

# dias_uteis = int(input("informe a qtd de dias uteis"))

# horas_trabalhadas = float(input("Horas trabalhadas"))

# salario_hora = float(input("Salario hora"))

# jornada = dias_uteis * 8

# valor_hora_extra = 0.0

# if horas_trabalhadas > jornada:
#     #tenhos horas extras pra calcular
#     horas_extras = horas_trabalhadas - jornada
#     valor_hora_extra = horas_extras * salario_hora * 1.5
#     horas_trabalhadas = jornada

# salario = horas_trabalhadas * salario_hora + valor_hora_extra

# print(f"Horas-extras: R${valor_hora_extra: .2f}")
# print(f"Salario total: R${salario: .2f}")


#exercicio 6


# A = int(input("Digite o primeiro numero:"))
# B = int(input("Digite o segundo numero:")) 
 

# num = A % B
# resultado = num
# if num == 0:
#     print(resultado"pode ser dividido")
# else:
#     print("não pode ser dividido")

# exercico 7

# import math

# num = float(input("Digite o numero:"))
# raiz = math.sqrt(num)

# print(f'A raiz quadrada de {num} é:{raiz}')

# exercicio 8 

# idade = int(input("Digite aqui sua idade:"))

# if idade < 5:
#     print("Não possui categoria")
# if idade >= 5 and idade <= 7:
#     print(f"{idade} você é juvenil")
# elif idade >= 8 and idade <=10:
#     print(f"{idade} você é juvenil")
# elif idade >= 11 and idade <= 15:
#     print(f"{idade} você é adolecete ")
# elif idade >= 16 and idade <= 30:
#     print(f"{idade} você é adulto")
# else:
#     print(f"{idade} Você é senhor")

#  exercicio 9

# num1 = float(input("Digite o primeiro numero:"))
# op = input("Operador (+,-,*,/)")
# num2 = float(input("Digite o segundo numero:"))

 

# if op == "+":
#     resultado = num1 + num2
# elif op == "-":
#     resultado = num1 - num2
# elif op == "*":
#     resultado= num1 * num2
# elif op == "/":
#     if num2 != 0:
#         resultado= num1 / num2
#     else:
#         print("Não é possivel resolver divisão por 0")
#         resultado = "Error"
# else:
#     print("Operador invalido ")
#     resultado = "Error"
    

# print(" Resposta ", resultado )

# exercicio 10

# import math

# a = float(input("Digite a: "))
# b = float(input("Digite b: "))
# c = float(input("Digite c: "))

# if a == 0:
#     print("Esta não é uma equação de 2 grau!")

# else:
#     delta = b * b - 4 * a * c
#     if delta < 0:
#         print(f"Não existem raízes reais para esta equação: {delta} é menor que 0")
#     else:
#         x1 = (-b + math.sqrt(delta)) / (2 * a)
#         x2 = (-b - math.sqrt(delta)) / (2 * a)
#         print(f"As raízes são: {x1} e {x2}")

# exercicio 11 prova 

# preco = float(input("Informe o preço de etiqueta: "))
# codigo = int(input("Opção de pagamento (1-4):"))

# match codigo:
#     case 1:
#         novo_preco = preco - preco * 0.1    #ou nov_preco = preco * 0.9
#         print(f"O valor a ser pago será de {novo_preco}")

#     case 2:
#         novo_preco = preco * 0.95
#         print(f"O valor a ser pago será de {novo_preco}")
    
#     case 3:
#         parcela = preco / 2
#         print(f"O valor a ser pago será de {preco} em 2x de {parcela}")

#     case 4:
#         novo_preco = preco * 1.07
#         parcela = novo_preco / 4
#         print(f"O valor a ser pago será de {novo_preco} em 4x de {parcela}")
    
#     case _: #default = quando codigo não é nenhum das opções listadas
#         print("Opção de pagamento inválida")

# preco = float(input("Informe o preço de etiqueta: "))
# codigo = int(input("Opção de pagamento (1, 2, 3, 4):"))


# if codigo == 1:
#     novo_preço = preco * 0.9
#     print(f"{novo_preço} esse é o valor com 10% de desconto")
# elif codigo == 2:
#     novo_preço = preco * 0.95
#     print(f"{novo_preço} esse é o valor com 5% de desconto")
# elif codigo == 3:
#     parcela = preco / 2
#     print(f"{parcela}valor da parcela sem juros")
# elif codigo == 4:
#     novo_preço = preco * 1.07
#     parcela = novo_preço / 4
#     print(f"{novo_preço} o valor com juros parcela de 4 vezes de {parcela}")
# else:
#     print("Opção de pagamento invalida")


# exercio 13 e 14

# dia = float(input("Digite o dia: "))
# mes = float(input("Digite o mês: "))
# ano = float(input("Digite o ano :"))

# num = ano % 4
# resultado = num


# if dia >= 1 and dia <= 30:
#     if mes != 2 and mes <= 12:
#         print("Sua data é valida")
#     elif mes == 2 and dia <= 28:
#         print("Sua data é valida ")
#     else:
#         print("tente novamente ")
# if num == 0:
#     print(f"{resultado} é um ano bissexto")
# else:
#     print("Não é um ano bissexto")



    
    

   


    



 





