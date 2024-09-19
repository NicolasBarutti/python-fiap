import oracledb

url = "oracle.fiap.com.br/orcl"
con = oracledb.connect(user='RM554944', dsn=url, password='030903')

cur = con.cursor()
sql_ins = '''update empregado set numero= :num, departamento= :depto 
            where nome= :nome'''
dado = {"nome": "Edson", "num": 87, 'depto': 'Engenharia'}

cur.execute(sql_ins, dado)
con.commit()
cur.close()
con.close()