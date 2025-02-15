from fastapi import APIRouter
from App.model.category_model import CategoryModel
from App.repository.category_repository import CategoryRepository

category_controller = APIRouter()

@category_controller.get('/category')
async def get_category():
  return CategoryRepository().get_categories()
