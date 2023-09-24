from pydantic import BaseModel

class Product(BaseModel):
    p_name: str
    price: int
    quantity: int
    imageurl: str
    category_id:int
