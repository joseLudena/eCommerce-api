from ....infrastructure.gateways.product_gateway import ProductGatewayImpl

class FindProductUseCase:
    def __init__(self, repository: ProductGatewayImpl):
        self.repository = repository

    def execute(self):
        return self.repository.get_all()