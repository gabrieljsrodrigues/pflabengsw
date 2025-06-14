# backend/src/database.py

import os
import pymysql
import pymysql.cursors
from dotenv import load_dotenv

load_dotenv() # Garante que as variáveis de ambiente sejam carregadas, mesmo que este módulo seja importado separadamente.

def validar_variaveis_ambiente():
    """
    Verifica se todas as variáveis de ambiente necessárias para a conexão com o banco de dados estão definidas.
    Levanta uma exceção se alguma variável estiver faltando.
    """
    # Mude os nomes das variáveis para os que o Railway fornece (MYSQL_...)
    required_vars = ["MYSQL_HOST", "MYSQL_PORT", "MYSQL_USER", "MYSQL_PASSWORD", "MYSQL_DATABASE"]
    for var in required_vars:
        if not os.getenv(var):
            raise Exception(f"Variável de ambiente {var} não definida")

def get_connection():
    """
    Retorna uma conexão PyMySQL com o banco de dados configurado nas variáveis de ambiente.
    Usa DictCursor para que os resultados das consultas (fetchall, fetchone) sejam dicionários (chave-valor).
    """
    # Remova ou comente esta linha se a validação estiver causando problemas no Railway.
    # Vamos focar em fazer a conexão principal funcionar primeiro.
    # validar_variaveis_ambiente() 

    try:
        conn = pymysql.connect(
            # Adapte os nomes das variáveis para os que o Railway fornece
            host=os.getenv("MYSQL_HOST"),
            # Adicione um valor padrão (3306) caso MYSQL_PORT seja None
            port=int(os.getenv("MYSQL_PORT", 3306)), 
            user=os.getenv("MYSQL_USER"),
            password=os.getenv("MYSQL_PASSWORD"),
            database=os.getenv("MYSQL_DATABASE"), # O nome da variável no Railway é MYSQL_DATABASE
            cursorclass=pymysql.cursors.DictCursor
        )
        return conn
    except Exception as e:
        # Imprime o erro para que você possa vê-lo nos logs do Railway
        print(f"Erro ao conectar ao banco de dados: {e}")
        # É importante relançar a exceção para que o FastAPI saiba que houve um problema
        raise e
