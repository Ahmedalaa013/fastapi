from fastapi import  status, HTTPException, APIRouter
from typing import Union
from src import controller
from src import models


router = APIRouter(
    prefix="/products",
    tags=['Products']
)

Product = models.Product



@router.get('/')
def get_all(category_id: Union[str, None] = None):
    data = controller.get_all_items("products",category_id)
    if not data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Product was not found")
    return {'data': data}


@router.get('/latest')
def get_latest():
    data = controller.get_latest_product()
    return {'data': data}


@router.get('/{id}')
def get_single_product(id: str):
    data = controller.get_single_product(id)
    if not data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Product was not found")
    return {"data": data}


@router.post('/')
def post_product(payload:Product):
    product = controller.create_product(payload)
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"error creating post")
    return {"product":product}
