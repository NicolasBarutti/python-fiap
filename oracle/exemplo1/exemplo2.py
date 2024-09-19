import oracledb

url = "oracle.fiap.com.br/orcl"
con = oracledb.connect(user='RM554944', dsn=url, password='030903')

cur = con.cursor()
sql_ins = '''insert into empregado(nome, cargo, salario, data_contratacao)
            values(:nome, :cargo, :salario, 
            to_date(:data,'YYYY-MM-DD'))'''
dado = {"nome": "Edson", "cargo": "gerente", 'salario': 3549.90, 
        'data': '2009-10-23'}

cur.execute(sql_ins, dado)
con.commit()
cur.close()
con.close()