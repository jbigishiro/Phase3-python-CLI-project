from simple_term_menu import TerminalMenu
from models import Supplier, Product
from prettycli import red, yellow, blue


class Cli():

    
    print(blue("WELCOME"))
    print(blue("Search for Products and their Suppliers"))

    def start(self):
  
        self.clear_screen()

        options = ["Search for product", "Add product","Delete Product" ,"Exit"]
        terminal_menu = TerminalMenu(options)
        menu_entry_index = terminal_menu.show()

        if options[menu_entry_index] == "Search for product":
            self.handle_search()
        elif options[menu_entry_index] == "Add product":
            self.handle_add()
        elif options[menu_entry_index] == "Delete Product":
            self.handle_delete()
        else:
            self.exit()

    
    def handle_search(self):
        
        self.clear_screen()

        options = ["Show all the products", " Search by product name", "Back"]
        terminal_menu = TerminalMenu(options)
        menu_entry_index = terminal_menu.show()

        if options[menu_entry_index] == "Show all the products":
            self.handle_show_all()
        elif options[menu_entry_index] == "Search by product name":
            self.handle_add()
        elif options[menu_entry_index] == "Back":
            self.start()

    def handle_show_all(self):

        self.clear_screen()            

        products = Product.show_all_products()

        if products:
            print(yellow("Products on sale:"))

            self.handle_print(products)
        else:
            print("No products are available.")

    def handle_print(self, products):

        for product in products:
                print(blue(f"Product: {product.name}"))
                print(f"Price: ${product.unit_price}")
                supplier = Supplier.find_user_by_seller_id(product.supplier_id)
                print(f"Sold by: {supplier.name}")


    def exit(self):

        self.clear_screen()
        print(blue("Goodbye!"))

    
    def clear_screen(self):

        print("\n")
     


app = Cli()
app.start()
