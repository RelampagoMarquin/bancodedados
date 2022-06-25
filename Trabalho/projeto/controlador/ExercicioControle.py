# Cadastra um novo Exercicio
def cadastrarExercicio(conexao, nome):
    cursor = conexao.cursor(buffered=True)
    sql = "INSERT INTO Exercicio(nome) VALUES (%s)"
    cursor.execute(sql, (nome, ))
    conexao.commit()

# Obtem exercicio por nome
def obterExercicioPorNome(conexao, nome):
    cursor = conexao.cursor(buffered=True)
    sql = "SELECT id FROM Exercicio WHERE nome=(%s)"
    cursor.execute(sql, (nome, ))
    id = cursor.fetchone()
    return id[0]
