from interactive_buttons import *

buttons = [
            Button(label="Continue", value="continue"),
            Button(label="Exit", value="exit")
          ]

comp = Component(buttons, text_color=Fore.BLACK, highlight_color=Back.GREEN)
choice = comp.matrix_buttons()
print(f"You chose: {choice}")
