
# exercicio 1
# soma = 0
# num = int(input("Informe o número da sequencia :"))

# while num != 0:
#     if num % 2 == 0:
#         soma = soma + 2
#     num = int(input("Informe o número da sequencia :"))

# print(soma)

#     print(f"Valor da soma vale {soma}")

# exercicio 2 e 3
# n = int(input("Informe a quantidade de alunos:"))

# contador = 0
# soma = 0 

# while contador < n:
#     nota = float(input("Informe a nota"))
#     soma = soma + nota
#     contador = contador + 1
# if nota >= 0 and nota <= 5:
#     nota = nota + 1
#     print(f"{nota}")
# elif nota > 5:
#     nota = nota + 1
#     print(f"{nota}")
    

# media = soma / n
# print(f"Na minha turma de 10 alunos a media foi {media}") 







# exercicio 5 

# n = int(input("Informe um númerointeiro positivo"))

# divisor = 1
# contaem_divisor = 0

# while divisor <= n:
#     if n % divisor == 0:
#           contagem_divisor = contagem_divisor + 1
#     divisor = divisor + 1

# print(f"{n} possui {contagem_divisor} divisores")    


# questao 7

# fahr = 50 

# while fahr <= 150:
#     celsius = 5/9*(fahr - 32)
#     print(f"{fahr:.1f} {celsius:.1f}")
#     fahr = fahr + 1

# questao 11

n = int(input("Informe n: "))

while n <= 0:
    n = int(input("Inválido, digite novamente: "))

if n == 1 or n == 2:
    print("Fibonacci vale 1")
else:
    ant = 1 
    atual = 1
    prox = ant + atual
    posicao = 3

while posicao < n:
    ant = atual
    atual = prox
    prox = ant + atual
    posicao = posicao + 1
print(f"Fibonacci vale {prox} ")
