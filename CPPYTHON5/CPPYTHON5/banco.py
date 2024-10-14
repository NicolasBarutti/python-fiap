import oracledb

# Função para conectar ao banco de dados Oracle
def conectar():
    return oracledb.connect(
        user="rm557914",
        password="210705",
        dsn="oracle.fiap.com.br/orcl"
    )

# Função para incluir uma nova mensagem no banco de dados
def inclui(mensagem: dict):
    conn = conectar()
    cursor = conn.cursor()

    sql = """
    INSERT INTO mensagens (assunto, destinatario, remetente, conteudo)
    VALUES (:1, :2, :3, :4)
    """
    cursor.execute(sql, (mensagem['assunto'], mensagem['destinatario'], mensagem['remetente'], mensagem['conteudo']))

    conn.commit()
    cursor.close()
    conn.close()

# Função para alterar uma mensagem existente no banco de dados
def altera(mensagem: dict):
    conn = conectar()
    cursor = conn.cursor()

    sql = """
    UPDATE mensagens
    SET assunto = :1, destinatario = :2, remetente = :3, conteudo = :4
    WHERE id = :5
    """
    cursor.execute(sql, (mensagem['assunto'], mensagem['destinatario'], mensagem['remetente'], mensagem['conteudo'], mensagem['id']))

    conn.commit()
    cursor.close()
    conn.close()

# Função para recuperar uma mensagem específica pelo ID
def recupera(id: int) -> dict:
    conn = conectar()
    cursor = conn.cursor()

    sql = "SELECT * FROM mensagens WHERE id = :1"
    cursor.execute(sql, (id,))
    resultado = cursor.fetchone()

    cursor.close()
    conn.close()

    if resultado:
        return {
            'id': resultado[0],
            'assunto': resultado[1],
            'destinatario': resultado[2],
            'remetente': resultado[3],
            'conteudo': resultado[4]
        }
    else:
        return None

# Função para recuperar mensagens por assunto usando LIKE
def recupera_assunto(assunto: str) -> list:
    conn = conectar()
    cursor = conn.cursor()

    sql = "SELECT * FROM mensagens WHERE assunto LIKE :1"
    cursor.execute(sql, ('%' + assunto + '%',))
    resultados = cursor.fetchall()

    cursor.close()
    conn.close()

    return [
        {
            'id': resultado[0],
            'assunto': resultado[1],
            'destinatario': resultado[2],
            'remetente': resultado[3],
            'conteudo': resultado[4]
        } for resultado in resultados
    ]

# Função para recuperar mensagens por destinatário
def recupera_destinatario(destinatario: str) -> list:
    conn = conectar()
    cursor = conn.cursor()

    sql = "SELECT * FROM mensagens WHERE destinatario = :1"
    cursor.execute(sql, (destinatario,))
    resultados = cursor.fetchall()

    cursor.close()
    conn.close()

    return [
        {
            'id': resultado[0],
            'assunto': resultado[1],
            'destinatario': resultado[2],
            'remetente': resultado[3],
            'conteudo': resultado[4]
        } for resultado in resultados
    ]

# Função para apagar uma mensagem pelo ID
def apaga(id: int):
    conn = conectar()
    cursor = conn.cursor()

    sql = "DELETE FROM mensagens WHERE id = :1"
    cursor.execute(sql, (id,))

    conn.commit()
    cursor.close()
    conn.close()
