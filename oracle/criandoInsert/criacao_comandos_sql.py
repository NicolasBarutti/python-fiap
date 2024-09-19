arq = open("municipio.txt", encoding='utf8')
saida = open("comandos.sql", encoding='utf8', mode="w")

dic = {}

for registro in arq:
    # print(registro)
    campos = registro.split(";")
    cod_uf = int(campos[1])
    uf = campos[0]
    cod_mun = int(campos[2])
    mun = campos[3]
    
    if not "'" in mun:



        # print(f"insert into estado (id,uf) values ({cod_uf}, {uf})")
        # print(f"insert into municipios values ({cod_mun}, {mun}, {cod_uf})")
        
        saida.write(f"insert into estado (id,uf) values ({cod_uf}, {uf})")
        saida.write("\n")
        saida.write(f"insert into municipios values ({cod_mun}, {mun}, {cod_uf})")
        saida.write("\n")   
saida.close()
         
