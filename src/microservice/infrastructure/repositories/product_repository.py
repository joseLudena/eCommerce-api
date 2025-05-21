from ..gateways.product_gateway import ProductGateway
from ..db.models.product_model import ProductModel
from sqlalchemy.orm import Session

class SQLProductRepository(ProductGateway):
    def __init__(self, db: Session):
        self.db = db

    def create(self, product: ProductModel):
        self.db.add(product)
        self.db.commit()
        self.db.refresh(product)
        return product

    def get_all(self):
        return self.db.query(ProductModel).all()
