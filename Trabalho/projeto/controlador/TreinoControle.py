from controlador.AlunoControle import obterAlunoPorNome
from controlador.ProfessorControle import obterProfessorPorNome
from controlador.ExercicioControle import *

# Vincula um treino a um Aluno
def VincularTreinoAoAluno(conexao, dia, descricao, aluno, professor):
    cursor = conexao.cursor(buffered=True)
    idAluno = obterAlunoPorNome(conexao, aluno)
    idProfessor = obterProfessorPorNome(conexao, professor)
    sql = "INSERT INTO Treino(idAluno, idProfessor, dia, descricao) \
        VALUES (%s, %s, %s, %s)"
    cursor.execute(sql, (idAluno, idProfessor, dia.casefold(), descricao))
    conexao.commit()

# Obtem id do treino pelo nome do aluno, professor e o dia
def obterTreinoPorAlunoEProfessorEDia(conexao, aluno, professor, dia):
    cursor = conexao.cursor(buffered=True)
    idAluno = obterAlunoPorNome(conexao, aluno)
    idProfessor = obterProfessorPorNome(conexao, professor)
    sql = "SELECT id FROM Treino WHERE idAluno = %s \
        AND idProfessor = %s AND dia = %s"
    cursor.execute(sql, (idAluno, idProfessor, dia.casefold()))
    treino = cursor.fetchone()
    return treino[0]

# Obtem o id do treino por aluno e descrição
def obterTreinoPorAlunoEdescricao(conexao, aluno, descricao):
    cursor = conexao.cursor(buffered=True)
    idAluno = obterAlunoPorNome(conexao, aluno)
    sql = "SELECT id FROM Treino WHERE idAluno = %s \
        AND descricao = %s"
    cursor.execute(sql, (idAluno, descricao))
    treino = cursor.fetchone()
    return treino[0]

# Adiciona um exercicio ao treino
def addExercicioAoTreino(conexao, aluno, descricao, exercicio, serie, repeticao):
    cursor = conexao.cursor(buffered=True)
    idTreino = obterTreinoPorAlunoEdescricao(conexao, aluno, descricao)
    idExercicio = obterExercicioPorNome(conexao, exercicio)
    sql = "INSERT INTO TreinoExercicio(idTreino, idExercicio, serie, repeticao) \
        VALUES (%s, %s, %s, %s)"
    cursor.execute(sql, (idTreino, idExercicio, serie, repeticao))
    conexao.commit()
    print('Treino vinculado com sucesso')

# Deleta um treino de um aluno
def removerTreinodoAluno(conexao, aluno, professor, dia):
    cursor = conexao.cursor(buffered=True)
    idTreino = obterTreinoPorAlunoEProfessorEDia(conexao, aluno, professor, dia)
    sql = "DELETE FROM treinoexercicio WHERE idTreino = %s"
    cursor.execute(sql, (idTreino,))
    sql = "DELETE FROM Treino WHERE id = %s"
    cursor.execute(sql, (idTreino,))
    conexao.commit()
    print('TREINO DELETADO COM SUCESSO')

# Mostra todos o treino de um alunos
def treinosDoAluno(conexao, aluno):
    cursor = conexao.cursor(buffered=True)
    idAluno = obterAlunoPorNome(conexao, aluno)
    sql = "SELECT descricao FROM Treino WHERE idAluno = %s"
    cursor.execute(sql, (idAluno, ))
    treino = cursor.fetchall()
    if len(treino) > 0:
        print('########### LISTA DE TREINO ##########')
        for t in treino:
            print(f'treino: {t[0]}')

# Mostra todos os exercicios, series e repetições de um treino 
def exerciciosDoAluno(conexao, aluno, descricao):
    cursor = conexao.cursor(buffered=True)
    idTreino = obterTreinoPorAlunoEdescricao(conexao, aluno, descricao)
    sql = "SELECT exercicio.nome, TreinoExercicio.serie, TreinoExercicio.repeticao \
            FROM Exercicio JOIN TreinoExercicio \
            ON TreinoExercicio.idExercicio = Exercicio.id \
            JOIN Treino ON TreinoExercicio.idTreino = Treino.id \
            WHERE Treino.id = %s"
    cursor.execute(sql, (idTreino, ))
    treino = cursor.fetchall()
    if len(treino) > 0:
        print('########### LISTA DE Exercicios ##########')
        for t in treino:
            (nome, serie, repeticao) = t
            print(f'Exercicio: {nome}\t Serie: {serie} \t repetição: {repeticao}')