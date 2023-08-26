from simple_term_menu import TerminalMenu
from models import Supplier, Product
from prettycli import red, yellow, blue


class Cli():

    def start(self):
        
        print("WELCOME")
        print("WELCOME")

        options = ["Login", "Sign Up", "Exit"]
        terminal_menu = TerminalMenu(options)
        menu_entry_index = terminal_menu.show()

        if options[menu_entry_index] == "Login":
            self.handle_login()
        elif options[menu_entry_index] == "Sign Up":
            self.handle_sign_up()
        else:
            self.exit()

app = Cli()
app.start()
