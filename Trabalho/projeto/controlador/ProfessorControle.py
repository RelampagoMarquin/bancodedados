# Cadastra um novo professor
def cadastrarProfessor(conexao, nome):
    cursor = conexao.cursor(buffered=True)
    sql = "INSERT INTO Professor(nome) VALUES (%s)"
    cursor.execute(sql, (nome, ))
    conexao.commit()

# Obtem o id do professor por nome
def obterProfessorPorNome(conexao, nome):
    cursor = conexao.cursor(buffered=True)
    sql = "SELECT id FROM Professor WHERE nome=(%s)"
    cursor.execute(sql, (nome, ))
    id = cursor.fetchone()
    return id[0]
