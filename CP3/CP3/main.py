from datetime import datetime


def exibir_menu():
    print(f"\n-MENU-")
    print("1.Inserir nova Consulta")
    print("2.Lista de Consultas Agendadas")
    print("3.Alterar Consultas Agendadas")
    print("4.Sair\n")

def inserir(list):
    nome = input("Digite o nome do paciente: ")
    dataConsulta = input("Digite a data da consulta: ")
    horarioConsulta = input("Digite o horário da consulta: ")
    list.append(nome)
    list.append(dataConsulta)
    list.append(horarioConsulta)

def listar_horarios():
    i = 0
    while i < len(listaCadastro):
        print(f"Nome: {listaCadastro[i]}, Data da consulta: {listaCadastro[i+1]}, Horario da consulta: {listaCadastro[i+2]}")
        i = i + 3

def sub_menu():
    selecao = int(input("Aperte 1.Para Alterar o Agendamento / Aperte 2.Para Remover o Agendamento "))
    if selecao == 1:
        i = 0
        n = 1
        while i < len(listaCadastro):
            print(f"{i}.{listaCadastro[i]}")
            i = i + 3

        alterar = int(input("Selecione um dos pacientes: "))
        for i in range(3):
            listaCadastro.pop(alterar)
        inserir(listaCadastro)

    elif selecao == 2:
        i = 0
        n = 1
        while i < len(listaCadastro):
            print(f"{i}.{listaCadastro[i]}")
            i = i + 3

        alterar = int(input("Selecione um dos pacientes: "))
        for i in range(3):
            listaCadastro.pop(alterar)

listaCadastro = []

while True:
    exibir_menu()
    escolha = input("Escolha uma das opções do MENU: ")
    if escolha == "1":
        inserir(listaCadastro)

    elif escolha == "2":
        listar_horarios()

    elif escolha == "3":
        sub_menu()


    elif escolha == "4":
        print("Saindo...")
        break
    else:
        print("Opção inválida, digite novamente: ")
