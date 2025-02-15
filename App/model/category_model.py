from pydantic import BaseModel, Field, StrictStr
from typing import Optional, Dict, List, Union, Tuple

class CategoryModel(BaseModel):
  codigo: int = Field()
  name: str = Field()
  tipo: str = Field()