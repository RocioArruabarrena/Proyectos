from decimal import Decimal

class ProductView:
    @staticmethod
    def display_product(name: str, price:Decimal, final_price:Decimal):
        print ("Producto:{name}")
        print ("Precio orginal: ${price:.2}")
        print ("Precio final con descuento: ${final_price:.2}")
        print ("-"* 30)
