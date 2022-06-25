from controlador.AlunoControle import *
from controlador.PlanoControle import *
from datetime import datetime

# Matricula um aluno (caso já tenha um numero de matricula só o plano será renovado)
def matricular(conexao, plano, aluno):
    cursor = conexao.cursor(buffered=True)
    idAluno = obterAlunoPorNome(conexao, aluno)
    idPlano = obterPlanoPorNome(conexao, plano)
    sql = "SELECT matricula From Aluno WHERE nome = %s"
    cursor.execute(sql, (aluno, ))
    matricula = cursor.fetchone()
    if matricula[0] != None:
        sql = "UPDATE Aluno SET dataMatricula = now(), idPlano = %s\
            WHERE id = %s"
        cursor.execute(sql, (idPlano, idAluno))    
    else:    
        matricula = datetime.today().strftime('%Y%m%d') + f"0{idAluno}"
        sql = "UPDATE Aluno SET dataMatricula = now(),  matricula = %s, idPlano = %s\
            WHERE id = %s"
        cursor.execute(sql, (matricula, idPlano, idAluno))
    conexao.commit()
    print(f'matricula feita com sucesso \nNUMERO DE MATRICULA: {matricula}')

# Retorna a data da matricula
def obterDataMatricula(conexao, aluno):
    cursor = conexao.cursor(buffered=True)
    sql = "SELECT dataMatricula FROM Aluno WHERE nome=(%s)"
    cursor.execute(sql, (aluno, ))
    data = cursor.fetchone()
    formato = [str(d) for d in data]
    return formato[0]

"""
    Altera a data da matricula Esse metodo não tem muita funcionaliade
exceto mudar a data de uma aluno para ele apareça lista de pagamento atrasado,
pois estou dropando banco sempre que ele inicia, desta forma não tem como altera
manualente quando rodar
"""
def alterdata(conexao, aluno):
    cursor = conexao.cursor(buffered=True)
    vigencia = obterVigencia(conexao, aluno)
    dataMatricula = obterDataMatricula(conexao, aluno)
    idAluno = obterAlunoPorNome(conexao, aluno)
    vigencia -= 2
    sql = "SELECT TIMESTAMPADD(MONTH, %s, %s) \
        FROM aluno WHERE id = %s"
    cursor.execute(sql, (vigencia, dataMatricula, idAluno))
    data = cursor.fetchone()
    formato = [str(d) for d in data]
    sql = "UPDATE Aluno SET dataMatricula = %s WHERE id = %s"
    cursor.execute(sql, (formato[0], idAluno))

