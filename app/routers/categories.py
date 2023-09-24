from fastapi import APIRouter
from src  import controller

router = APIRouter(
    prefix="/categories",
    tags=['Categories']
)

@router.get('/')
def get_all_categories():
    data = controller.get_all_items("category")
    return {'data': data}