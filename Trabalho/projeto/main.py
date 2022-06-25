from imports import *

# Iniciando o banco
conexao = criarBanco()
criarTabelas(conexao)

# Cadastrando Plano
cadastrarPlano(conexao, 'ANUAL', 348.00, 12)
cadastrarPlano(conexao, 'MENSAL', 30.00, 1)

# Cadastrando Aluno
cadastrarAluno(conexao, 'João Cena', '555')
cadastrarAluno(conexao, 'Charlote', '5568')
cadastrarAluno(conexao, 'Undertaker', '55963')
cadastrarAluno(conexao, 'HHH', '23555')

# Matriculando os alunos
matricular(conexao, 'MENSAL', 'Charlote')
matricular(conexao, 'MENSAL', 'João Cena')
matricular(conexao, 'ANUAL', 'HHH')
matricular(conexao, 'ANUAL', 'Undertaker')

# Cadastrando um professor
cadastrarProfessor(conexao, 'The Pedra')

# Cadastrar Exercicio
cadastrarExercicio(conexao, 'rosca')
cadastrarExercicio(conexao, 'supino')

# Vincular Treino ao aluno
VincularTreinoAoAluno(conexao, 'segunda', 'DIA DO BRAÇO', 'Charlote', 'The Pedra')
VincularTreinoAoAluno(conexao, 'segunda', 'bicipes', 'João Cena', 'The Pedra')

# Adicionando Exercicio ao treino
addExercicioAoTreino(conexao, 'João Cena', 'bicipes', 'rosca', 15, 3)
addExercicioAoTreino(conexao, 'Charlote', 'DIA DO BRAÇO', 'rosca', 10, 3)
addExercicioAoTreino(conexao, 'Charlote', 'DIA DO BRAÇO', 'supino', 12, 3)

# Exibir treinos do Aluno
treinosDoAluno(conexao, 'João Cena')
treinosDoAluno(conexao, "Charlote")

# Remove treino do Aluno
removerTreinodoAluno(conexao, 'João Cena', 'The Pedra', 'segunda')

# Mostra todos os exercicios de um treino de aluno
exerciciosDoAluno(conexao, 'Charlote', 'DIA DO BRAÇO')

# Mudando a data de matricula para cair na lista de devedores
alterdata(conexao, 'Charlote')

# Lista todos os alunos que não pagaram
madarAgiota(conexao)

# Lista todos os alunos ativos
MostarAlunosAtivos(conexao, 'MENSAL')

# Mostra o faturamento
faturamento(conexao)

# Mostra o plano mais rentavel
maisRentavel(conexao)