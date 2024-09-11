try:
    a = int(input("A:"))
    b = int(input("B:"))
    c = a / b
except (ZeroDivisionError, ValueError) as e:
    print("Erro", type(e))
else:
    print(f"valor é igual {c}")