from decimal import Decimal

class Product:
    def __init__(self, name:str, price: Decimal, discount_strategy):
        self.name = name
        self.price = price
        self.discount_strategy = discount_strategy
    
    def get_final_price(self)-> Decimal:
        return self.discount_strategy.apply_discount(self.price)
    
    def set_discount_strategy (self,strategy):
        self.discount_strategy = strategy
    