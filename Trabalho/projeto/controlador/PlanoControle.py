# Cadastra um novo Plano
def cadastrarPlano(conexao, nome, preco, vigencia):
    cursor = conexao.cursor(buffered=True)
    sql = "INSERT INTO Plano(nome, preco, vigencia) VALUES (%s, %s, %s)"
    cursor.execute(sql, (nome, preco, vigencia))
    conexao.commit()

# Retorna o Id do Plano de acordo com o nome    
def obterPlanoPorNome(conexao, nome):
    cursor = conexao.cursor(buffered=True)
    sql = "SELECT id FROM Plano WHERE nome=(%s)"
    cursor.execute(sql, (nome, ))
    id = cursor.fetchone()
    return id[0]

# Retona o nome de todos os Planos
def todosPlanos(conexao):
    cursor = conexao.cursor()
    sql = "SELECT nome FROM Plano"
    cursor.execute(sql)
    return cursor.fetchall()
