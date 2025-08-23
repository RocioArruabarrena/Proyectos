from decimal import Decimal

class Product:
    def __init__(self, name: str, price: Decimal, discount_strategy):
        self.name = name
        self.price = price
        self.discount_strategy = discount_strategy
    
    def get_final_price(self) -> Decimal:
        # Por defecto usamos process()
        return self.discount_strategy.process(self.price)
    
    def get_final_price_legacy(self) -> Decimal:
        # También disponible con apply_discount()
        return self.discount_strategy.apply_discount(self.price)
    
    def set_discount_strategy(self, strategy):
        self.discount_strategy = strategy

    