sorteada = "frango assado"
erros = 0

segredo = ""

for c in sorteada :
    if c == ' ':
        segredo = segredo + "  "
    else:
        segredo += "_ "
    
   

print(f"{segredo} \nerros: {erros}")
letra = input("Informe a letra: ").lower

segredo = ""

for c in sorteada:
    if c == ' ' :
        segredo = segredo + "   "
    elif c == letra:
        segredo = segredo + c + " "
    else:
        segredo = segredo + "_ "
        
print(f"{segredo}\nerros: {erros}")