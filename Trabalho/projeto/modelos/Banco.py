import mysql.connector
#inicializando o banco
def criarBanco():
    BD_CONFIG = {
        "host": "localhost",
        "user": "root",
        "password": "123456"
    }

    # Conexao com o serviço do MySQL
    conexao = mysql.connector.connect(** BD_CONFIG)
    cursor = conexao.cursor()

    # Criar o banco Academia
    cursor.execute("drop database if exists Academia")
    cursor.execute("create database if not exists Academia")
    cursor.execute("use Academia")

    return conexao
