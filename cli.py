from simple_term_menu import TerminalMenu
from models import Supplier, Product
from prettycli import red, yellow, blue


class Cli():
   
    print(blue("WELCOME"))
    print(blue("Search for Products and their Suppliers"))

    def start(self):
  
        while True:
            self.clear_screen()

            options = ["Search for product", "Add product","Update product price", "Delete Product" ,"Exit"]
            terminal_menu = TerminalMenu(options)
            menu_entry_index = terminal_menu.show()

            if options[menu_entry_index] == "Search for product":
                self.handle_search()
            elif options[menu_entry_index] == "Add product":
                self.handle_add()
            elif options[menu_entry_index] == "Update product price":
                self.handle_update()
            elif options[menu_entry_index] == "Delete Product":
                self.handle_delete()
            else:
                self.exit()
                break

    
    def handle_search(self):
        self.clear_screen()

        search_product = input("Enter the product name: ")
        products = Product.find_product_by_name(search_product)

        matching_products = []
        for product in products:
            if search_product == product.name:
                matching_products.append(product)

        if matching_products:
            print(yellow("Matching products:"))
            self.handle_print(matching_products)
        else:
            print(red("Product not found."))

    def handle_add(self,):
        self.clear_screen()

        name = input("Product name: ")
        unit_price = input("Unit price: ")
        supplier_id=input("Supplier ID:")
        # use while loop to check if price is a valid number
        while True:
            if unit_price.isdigit():
                break
            else:
                print(red("Invalid price. Please enter a valid number."))

        Product.add_product(name, unit_price, supplier_id)
        print(yellow("Product added."))


    def handle_update(self):

        self.clear_screen()

        product_id = input("Enter the product ID: ")
        new_price = input("Enter the new unit price: ")
    
        Product.update_price(product_id, new_price)
        print(yellow("Product price updated successfully."))


    def handle_delete(self):

        self.clear_screen()

        product_id = input(yellow("Enter the ID of the product you want to remove: "))               
        product = Product.find_product_by_id(product_id)

        if not product:
            print(yellow("Product not found."))
        else:
            Product.delete_item_by_id(product_id)
            print(red("Product removed."))


    def handle_print(self, products):
        for product in products:
                print((f"Item: {product.name}"))
                print(f"Unit Price: {product.unit_price} $")
                supplier = Supplier.search_supplier_by_id(product.supplier_id)    
                print(f"Sold by: {supplier.name}")

    def exit(self):
        self.clear_screen()
        print(blue("Goodbye!"))
    
    def clear_screen(self):
        print("\n")
     


app = Cli()
app.start()
