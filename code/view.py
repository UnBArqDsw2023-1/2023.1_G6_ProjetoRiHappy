class ShoppingCartView:
    def get_user_choice(self):
        print("1. Add Product")
        print("2. Display Cart Contents")
        print("3. Display Cart Total")
        print("4. Quit")

        try:
            choice = int(input("Enter your choice: "))
            return choice
        except ValueError:
            return -1

    def get_product_details(self):
        name = input("Enter product name: ")
        price = float(input("Enter product price: "))
        return Product(name, price)

    def display_message(self, message):
        print(message)

    def display_cart_contents(self, cart_items):
        if not cart_items:
            print("The cart is empty.")
        else:
            print("Cart Contents:")
            for product in cart_items:
                print(product.get_name(), "$%.2f" % product.get_price())