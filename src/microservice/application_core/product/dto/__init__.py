from pydantic import BaseModel

class ProductCreateDTO(BaseModel):
    name: str
    stock: int
    price: float
    img: str
    description: str
