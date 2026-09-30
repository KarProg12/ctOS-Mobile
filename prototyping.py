from pick import pick

# Definiujemy opcje i tytuł menu
title = "Choose an option: "
options = ["Continue", "Exit"]

# Wyświetlamy menu (działa na Windows i Linux/Termux)
option, index = pick(options, title, indicator=">")

choice = option.lower()
print(f"You chose: {choice}")