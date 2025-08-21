from abc import ABC, abstractmethod
from decimal import Decimal

class DiscountStrategy (ABC):
    @abstractmethod
    def apply_discount (self, price:Decimal) -> Decimal:
        pass


class NoDiscount(DiscountStrategy):
    def apply_discount (self, price:Decimal) -> Decimal:
        return price

class PercentageDiscount(DiscountStrategy):
    def __init__(self, percent:Decimal):
        self.percent = percent
    
    def apply_discount(self, price:Decimal) -> Decimal:
        return price * (1- self.percent/100)

class FixedDiscount(DiscountStrategy):
    def __init__(self, amount:Decimal):
        self.amount = amount
    
    def apply_discount(self, price:Decimal) -> Decimal:
        return max (0, price - self.amount)

        
    