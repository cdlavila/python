from injector import Injector, inject, Module

class Logger:
    @staticmethod
    def log(message):
        print("Logging:", message)

class ProductService:
    @inject
    def __init__(self, logger: Logger):
        self.logger = logger

    def create_product(self, name):
        self.logger.log(f"Creating product: {name}")

class AppModule(Module):
    @staticmethod
    def configure(binder, **kwargs):
        binder.bind(Logger, to=Logger)

injector = Injector([AppModule()])
product_service = injector.get(ProductService)
product_service.create_product("Widget")
