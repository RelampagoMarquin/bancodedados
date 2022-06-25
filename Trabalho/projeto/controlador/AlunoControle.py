# Cadastra um novo Aluno
def cadastrarAluno(conexao, nome, telefone):
    cursor = conexao.cursor()
    sql = "INSERT INTO Aluno(nome, telefone) VALUES (%s, %s)"
    cursor.execute(sql, (nome, telefone))
    conexao.commit()

# Buscar o ID de um aluno por Nome
def obterAlunoPorNome(conexao, nome):
    cursor = conexao.cursor(buffered=True)
    sql = "SELECT id FROM Aluno WHERE nome=(%s)"
    cursor.execute(sql, (nome, ))
    id = cursor.fetchone()
    return id[0]

# Obtem o id do plano do aluno
def obterPlanodoAluno(conexao, nome):
    cursor = conexao.cursor(buffered=True)
    sql = "SELECT idPlano FROM Aluno WHERE nome=(%s)"
    cursor.execute(sql, (nome, ))
    id = cursor.fetchone()
    return id[0]

# Obter tempo de vigencia de contrato por aluno
def obterVigencia(conexao, aluno):
    cursor = conexao.cursor(buffered=True)
    idPlano = obterPlanodoAluno(conexao, aluno)
    sql = "SELECT vigencia FROM Aluno \
            JOIN Plano ON Aluno.idPlano = Plano.id \
            WHERE idPlano=(%s)"
    cursor.execute(sql, (idPlano, ))
    vigencia = cursor.fetchone()
    return vigencia[0]

# Obter todos os alunos
def todosAlunos(conexao):
    cursor = conexao.cursor()
    sql = "SELECT nome FROM ALuno"
    cursor.execute(sql)
    return cursor.fetchall()
