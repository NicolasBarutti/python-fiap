
def cadastra(conj: list):
    tit = input("Informe o titulo:")
    cat = input("Informe a categoria:")
    sin = input("Sinopse: ")
    aut = input("Autor(es): ")
    edi = input("Editora: ")
    prc = float(input("Preço:"))
    livro = [tit, cat, sin, aut, edi, prc]
    conj.append(livro)

def consulta(conj : list):
    resultado = []
    cat = input("Informe a categoria: ")
    for i in range(len(conj)):
        if conj [i][1] == cat:
            resultado.append(conj[i])

    if len(resultado) == 0:
        print("nenhum livro encontrado!")
    else:
        for livro in resultado:
            print(livro)

def busca (conj : list, titulo: str):
    for i in range(len(conj)):
        if conj[i][0] == titulo:
            return i
    return - 1

def altera(conj : list):
    tit = input("Informe o titulo do livro que deseja alterar: ")
    pos = busca(conj,tit)
    if pos == -1:
        print("Não encontrei o livro com este titulo! ")
    else:
        rotulos = ["Titulo", "Categoria", "Sinopse", "Autor(es)","Editora", "Preço"]
        for i in range(len(rotulos)):
            aux = input(f"{rotulos[i]} ({conj [pos] [i]}: )")
            if len(aux) > 0:
                if rotulos[i] == "Preço":
                    conj[pos][i] = float(aux)
                else:
                    conj[pos][i] = aux
       
        
        aux = input(f"Categoria({conj [pos] [1]}: )")
        if len(aux) > 0:
            conj[pos] [1] = aux
        
        aux = input(f"Titulo({conj [pos] [3]}: )")
        if len(aux) > 0:
            conj[pos] [2] = aux
        
    

def exclui (conj: list):
    tit = input("Informe o titulo do livro que deseja  excluir")
    pos = busca(conj, tit)
    if pos == -1:
        print("Naõ há livrod com este titulo!")
    else:
        print(conj[pos])
        print("Livro excluido com sucesso!")
        conj.pop(pos)


estoque = []

opcao = 0
while opcao != 6:
    print("     SISTEMA DE LIVRARIA     ")
    print("1 - Cadastrar")
    print("2 - Consulta")
    print("3 - Altera")
    print("4 - Exclui")
    print("5 - Sair")
    try:
        opcao = int(input("Iforme uma opção"))
    except Exception:
        ("Opcão invalida!")
        opcao = 0

    if opcao == 1:
        cadastra(estoque)
    elif opcao == 2:
        consulta(estoque)
    elif opcao == 3:
        altera(estoque)
    elif opcao == 4:
        exclui(estoque)
        