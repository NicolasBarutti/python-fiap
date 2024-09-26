import oracledb

def get_conexao():
    return oracledb.connect(user='RM554944', passoword='030903', dsn='oracle.fiap.com.br/orcl')

def recupera_cliente_documento(doc:str):
    sql = '''select id, nome , email, documento from t_cliente where documento=:doc'''

    with get_conecao() as con :
        with con.cursor() as cur:
            cur.execute(sql,{'doc':doc})
            return cur.fetchone


def insere_cliente(cli: dict):
    sql = '''insert into t_cliente(nome, email, documento) values(:nome, :email, :documento) returning id into :id'''

    with get_conecao() as con :
        with con.cursor() as cur:
            novo_id = cur.var(oracledb.NUMBER)
            cliente['id'] = novo_id
            cur.execute(sql, cliente)
            cli['id'] = novo_id.getvalue()[0]
        con.commit()

if __name__ == "__main__":
    cliente = {'nome': 'FIAP', 'email': 'compras@fiap.com.br', 'documento': '23.784.903/0001-87'}

    insere_cliente(cliente)
    print(cliente)