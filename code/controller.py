from model import Product
from view import ShoppingCartView

class ShoppingCartController:
    def __init__(self):
        self.shopping_cart = []
        self.view = ShoppingCartView()

    def run(self):
        while True:
            choice = self.view.get_user_choice()
            
            if choice == 1:
                product = self.view.get_product_details()
                self.shopping_cart.append(product)
                self.view.display_message("Product added to the cart.")
            
            elif choice == 2:
                self.view.display_cart_contents(self.shopping_cart)
            
            elif choice == 3:
                total = self.calculate_cart_total()
                self.view.display_message("Total: $%.2f" % total)
            
            elif choice == 4:
                self.view.display_message("Thank you for using the shopping cart!")
                break
            
            else:
                self.view.display_message("Invalid choice. Please try again.")

    def calculate_cart_total(self):
        total = 0
        for product in self.shopping_cart:
            total += product.get_price()
        return total