import oracledb

url = "oracle.fiap.com.br/orcl"
con = oracledb.connect(user='RM554944', dsn=url, password='030903')

cur = con.cursor()
sql_ins = '''insert into empregado(autor, titulo, tipo, avaliacao , data_lancamento)
            values(:autor, :titulo, :tipo,:avaliacao, 
            data_lancamento(:data,'YYYY-MM-DD'))'''
dado = {"autor": "Edson", "titulo": "Harry", "tipo": "terror", 'avaliacao': 10, 
        'data': '2009-10-23'}

cur.execute(sql_ins, dado)
con.commit()
cur.close()
con.close()