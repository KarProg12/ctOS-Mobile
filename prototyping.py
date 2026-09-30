from simple_term_menu import TerminalMenu

# Definiujemy opcje menu
options = ["Continue", "Exit"]

# Tworzymy interaktywne menu w terminalu
terminal_menu = TerminalMenu(options)
menu_entry_index = terminal_menu.show()

# Pobieramy wybraną opcję i zmieniamy na małe litery
choice = options[menu_entry_index].lower()
print(f"You chose: {choice}")

