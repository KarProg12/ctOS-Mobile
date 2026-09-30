import inquirer

questions = [
    inquirer.List(
        'choice',
        message="Choose an option",
        # 'interactive' buttons in terminal
        choices=['Continue', 'Exit'],
        hints={'Continue': 'Press enter to continue',
               'Exit': 'Press enter to exit'} ,
        # carousel=True - pointer jumps e.g. from bottom to the top
        # carousel=False - pointer doesn't jump from any max top or bottom position
        carousel=True
    )
]

answers = inquirer.prompt(questions)

# save choice in choice variable and print info for user
choice = answers['choice'].lower()
print(f"You chose: {choice}")
