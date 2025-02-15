from App.dependencias.database import ConexaoPostgres


class CategoryRepository:
  def __init__(self):
    self.cx = ConexaoPostgres()

  def get_categories(self):
    return  self.cx.select("SELECT * FROM CATEGORIES;")
