import oracledb

def get_conexao():
    url = "oracle.fiap.com.br/orcl"
    return oracledb.connect(user="RM554944", password="030903", dsn=url)


def insere_filme(filme: dict):
    sql = '''insert into t_filme(titulo, diretor, duracao, avaliacao,
            sinopse, classificacao, genero, data_lancamento)
            values(:titulo, :diretor, :duracao, :avaliacao,
            :sinopse, :classificacao, :genero,
            to_date(:data_lancamento, 'YYYY-MM-DD'))'''
    
    with get_conexao() as con:
        with con.cursor() as cur:
            cur.execute(sql, filme)
        con. commit()

def consulta_genero(genero: str) -> list:
    sql = "select* from t_filme where genero like :gen"
    with get_conexao() as con:
        with con.cursor() as cur:
            cur.execute(sql, {"gen": f"%{genero}%"})
            lista = cur. fetchall()
            return lista
        
def altera_filme(filme:dict):
    