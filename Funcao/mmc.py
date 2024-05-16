def mmc( a, b):
     x = b
    while x % a != 0:
        x = x + b


a = int(input("Informe o numero a: "))
b = int(input("Informe o numero b: ")) 

x = b

while x % a != 0:
    x = x + b

print (f"{a} {b}")
