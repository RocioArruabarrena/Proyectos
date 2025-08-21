from src.domain.models.discount_strategy import NoDiscount, PercentageDiscount, FixedDiscount
from src.domain.models.product import Product
from src.views.product_view import ProductView
from src.controller.product_controller import ProductController

if __name__ == "__main__":
    product = Product("Café Zeppe", 100.0, NoDiscount())
    view = ProductView()
    controller = ProductController(product, view)

    controller.update_view()

    
    controller.change_discount(PercentageDiscount(20))
    controller.update_view()

    controller.change_discount(FixedDiscount(15))
    controller.update_view()
