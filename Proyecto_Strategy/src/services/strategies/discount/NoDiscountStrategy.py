from decimal import Decimal
from strategies import DiscountStrategy

class NoDiscount(DiscountStrategy):
    def apply_discount(self, price: Decimal) -> Decimal:
        return price

    def process(self, price: Decimal) -> Decimal:
        return price