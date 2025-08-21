from models.product import Product
from views.product_view import ProductView

class ProductController:
    def __init__(self, product: Product, view: ProductView):
        self.product = Product
        self.view = ProductView
    
    def update_view (self):
        final_price = self.product.get_final_price ()
        self.view.display_product(self.product.name,self.product.price, final_price)
    
    def change_discount(self, discount_strategy):
        self.product.set_discount_strategy (discount_strategy)