import interactive_buttons
from interactive_buttons import Button, Component, ButtonStyle, HACKER_STYLE

buttons = [
            Button(label="Continue", value="continue"),
            Button(label="Exit", value="exit")
          ]

comp = Component(buttons, global_buttons_style=ButtonStyle(**HACKER_STYLE))
choice = comp.column_buttons()
print(f"You chose: {choice}")
