# Criar as tabelas
def criarTabelas(conexao):
    cursor = conexao.cursor()
    TABELAS = {}
    TABELAS["Plano"] = """
    create table if not exists Plano (
        id integer auto_increment,
        nome varchar(120) not null,
        preco float not null,
        vigencia int not null,
        primary key (id)
    )"""

    TABELAS["Aluno"] = """
    create table if not exists Aluno (
        id integer auto_increment,
        nome varchar(120) not null,
        telefone varchar(14) not null,
        matricula varchar(14),
        dataMatricula timestamp,
        idPlano int,
        primary key (id),
        foreign key (idPlano)
            references Plano(id),
        unique(matricula)
    )"""

    TABELAS["Professor"] = """
    create table if not exists Professor (
        id integer auto_increment,
        nome varchar(120),
        primary key (id)
    )"""

    TABELAS["Exercicio"] = """
    create table if not exists Exercicio (
        id integer auto_increment,
        nome varchar(50),
        primary key (id)
    )"""

    TABELAS["Treino"] = """
    create table if not exists Treino (
        id integer auto_increment,
        dia char(7),
        descricao varchar(120),
        idAluno int,
        idProfessor int,
        primary key (id),
        foreign key (idAluno)
            references Aluno(id),
        foreign key (idProfessor)
            references Professor(id)
    )"""

    TABELAS["TreinoExercicio"] = """
    create table if not exists TreinoExercicio (
        id integer auto_increment,
        serie int,
        repeticao int,
        idExercicio int,
        idTreino int,
        primary key (id),
        foreign key (idTreino)
            references Treino(id),
        foreign key (idExercicio)
            references Exercicio(id)
    )"""

    for i in TABELAS:
        cursor.execute(TABELAS[i])
        print(f"Criando a tabela {i}")