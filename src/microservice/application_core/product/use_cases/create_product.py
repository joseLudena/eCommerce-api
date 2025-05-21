from ....infrastructure.db.models.product_model import ProductModel
from ....infrastructure.gateways.product_gateway import ProductGateway


class CreateProductUseCase:
    def __init__(self, repository: ProductGateway):
        self.repository = repository

    def execute(self, name: str, stock: int, price: float, img: str, description: str):
        product = ProductModel(
            name=name, stock=stock, price=price, img=img, description=description
        )
        return self.repository.create(product)
