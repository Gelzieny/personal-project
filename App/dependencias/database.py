import psycopg2
from psycopg2 import sql, DatabaseError
import os
from dotenv import load_dotenv

# Carregar variáveis de ambiente do arquivo .env
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
          return cursor.fetchall()
    except DatabaseError as e:
      print(f"Erro ao executar query: {e}")
      return {"success": False, "error": str(e)}