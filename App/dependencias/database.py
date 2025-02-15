import psycopg2
from psycopg2 import DatabaseError
import os
from dotenv import load_dotenv

load_dotenv()

class ConexaoPostgres:
  def __init__(self):
    """Inicializa os parâmetros de conexão"""
    self.database = {
      "dbname": os.getenv("POSTGRES_DB", "mydatabase"),
      "user": os.getenv("POSTGRES_USER", "docker"),
      "password": os.getenv("POSTGRES_PASSWORD", "docker"),
      "host": os.getenv("POSTGRES_HOST", "localhost"),
      "port": os.getenv("POSTGRES_PORT", "5432"),
    }

  def executar_query(self, query, params=None, commit=False):
    """Executa uma query no banco de dados"""
    try:
      with psycopg2.connect(**self.database) as conn:
        with conn.cursor() as cursor:
          cursor.execute(query, params)
          if commit:
            conn.commit()
            return {"success": True, "rows_affected": cursor.rowcount}
          # Recupera os resultados da consulta como lista de dicionários
          return self.dictfetchall(cursor)  # Passando o cursor para o dictfetchall
    except DatabaseError as e:
      print(f"Erro ao executar query: {e}")
      return {"success": False, "error": str(e)}

  def dictfetchall(self, cursor):
    """Recupera os dados da consulta como uma lista de dicionários"""
    columns = [col[0] for col in cursor.description]  # Usando cursor recebido como argumento
    rows = cursor.fetchall()
    # Transforma cada linha em um dicionário
    return [dict(zip(columns, row)) for row in rows]

  def select(self, query, params=None):
    """Executa uma query de seleção no banco de dados"""
    return self.executar_query(query, params)

  def teste(self) -> str:
    r = self.select("SELECT 1;") # Executa uma query de teste   
    resultado = r[0]['?column?']

    return {
      "status": "success" if resultado == 1 else "error",
      "resultado": "Conexão bem sucedida" if resultado == 1 else "Falha na conexão"
    }

    