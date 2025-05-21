from abc import ABC, abstractmethod
from ...infrastructure.db.models.product_model import ProductModel
from sqlalchemy.orm import Session

class ProductGateway(ABC):
    @abstractmethod
    def create(self, product: ProductModel):
        pass

class ProductGatewayImpl(ProductGateway):
    def __init__(self, db: Session):
        self.db = db

    def create(self, product: ProductModel):
        self.db.add(product)
        self.db.commit()
        self.db.refresh(product)
        return product

    def get_all(self, product: ProductModel):
        return self.db.query(product).all()
