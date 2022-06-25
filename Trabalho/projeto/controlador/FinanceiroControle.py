from controlador.MatriculaControle import *

# Mostra qual o plano é mais rentavel
def maisRentavel(conexao):
    planos = todosPlanos(conexao)
    rendaM = 0
    rendaA = 0
    nomePlano = ''
    for plano in planos:
        cursor = conexao.cursor(buffered=True)
        sql = "SELECT preco FROM Plano Where nome = %s"
        cursor.execute(sql, (plano[0], ))
        valor = cursor.fetchone()
        alunos = planoAtivo(conexao, plano[0])
        if len(alunos) > 0:
            vigencia = obterVigencia(conexao, alunos[0])
            valorAux = len(alunos) * valor[0] / vigencia
            if(valorAux > rendaM):
                rendaM = valorAux
                rendaA = rendaM * 12
                nomePlano = plano
    print(f'######PLANO MAIS RENTAVEL#######\nPlano: {nomePlano[0]}\n\
valor mensal: {rendaM}\nvalor anual: {rendaA}')

# Mostra o faturamento mensal da acedemia
def faturamento(conexao):
    planos = todosPlanos(conexao)
    renda = 0
    for plano in planos:
        cursor = conexao.cursor(buffered=True)
        sql = "SELECT preco FROM Plano Where nome = %s"
        cursor.execute(sql, (plano[0], ))
        valor = cursor.fetchone()
        alunos = planoAtivo(conexao, plano[0])
        if len(alunos) > 0:
            vigencia = obterVigencia(conexao, alunos[0])
            renda += len(alunos) * valor[0] / vigencia
    print('####### FATURAMENTO MENSAL #######')
    print(renda)

# mostar o numero de pessoas em atraso
def madarAgiota(conexao):
    alunos = todosAlunos(conexao)
    velhacos = []
    for aluno in alunos:
        dataMatricula = obterDataMatricula(conexao, aluno[0])
        idAluno = obterAlunoPorNome(conexao, aluno[0])
        vigencia = obterVigencia(conexao, aluno[0])
        vencido = checarData(conexao, dataMatricula, idAluno, vigencia)
        if vencido:
            velhacos.append(aluno[0])
    print('##########LISTA DE VELHACO##########')
    for velhaco in velhacos:
        
        print(f"Nome: {velhaco}")

# Retorna se a mensalidade esta vencida ou não
def checarData(conexao, dataMatricula, idAluno, vigencia):
    cursor = conexao.cursor(buffered=True)
    sql = "SELECT ADDDATE(%s, INTERVAL %s MONTH) \
        FROM aluno WHERE id = %s"
    cursor.execute(sql, (dataMatricula, vigencia, idAluno))
    data = cursor.fetchone()
    formato = [str(d) for d in data]
    sql = "SELECT TIMESTAMPDIFF(MONTH, %s, %s) \
            FROM Aluno WHERE id = %s"
    cursor.execute(sql, (dataMatricula, formato[0], idAluno))
    limite = cursor.fetchone()
    sql = "SELECT TIMESTAMPDIFF(MONTH, %s, now()) \
            FROM Aluno WHERE id = %s"
    cursor.execute(sql, (dataMatricula, idAluno))
    passando = cursor.fetchone()
    if (limite[0] <= passando[0]):
        vencido = True
    else:
        vencido = False
    return vencido

# Retorna a lista de todos os alunos com plano ativo
def planoAtivo(conexao, plano):
    cursor = conexao.cursor(buffered=True)
    idPlano = obterPlanoPorNome(conexao, plano)
    sql = "SELECT nome FROM Aluno WHERE idPlano = %s"
    cursor.execute(sql, (idPlano, ))
    alunos = cursor.fetchall()
    honestos = []
    for aluno in alunos:
        dataMatricula = obterDataMatricula(conexao, aluno[0])
        idAluno = obterAlunoPorNome(conexao, aluno[0])
        vigencia = obterVigencia(conexao, aluno[0])
        vencido = checarData(conexao, dataMatricula, idAluno, vigencia)
        if not vencido:
            honestos.append(aluno[0])
    return honestos

# Mostar todos os alunos que estão com plano ativo
def MostarAlunosAtivos(conexao, plano):
    print('#########LISTA DE BOM PAGADOR#########')
    alunos = planoAtivo(conexao, plano)
    for aluno in alunos:
        print(aluno)