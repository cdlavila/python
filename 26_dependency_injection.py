# Dependency
class Logger:
    @staticmethod
    def log(message):
        print("Logging:", message)


# Without Dependency Injection
class ProductServiceWithoutDI:
    def __init__(self):
        self.logger = Logger()

    def create_product(self, name):
        self.logger.log(f"Creating product: {name}")

product_service = ProductServiceWithoutDI()
product_service.create_product("Without DI")


# With Dependency Injection
class ProductServiceWithDI:
    def __init__(self, logger):
        self.logger = logger

    def create_product(self, name):
        self.logger.log(f"Creating product: {name}")

logger = Logger()
product_service = ProductServiceWithDI(logger)
product_service.create_product("With DI")