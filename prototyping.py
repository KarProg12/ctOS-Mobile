import inquirer

questions = [
    inquirer.List(
        'choice',
        message="Choose an option",
        choices=['Continue', 'Exit'],
        carousel=True
    )
]

answers = inquirer.prompt(questions)

# Wyciągamy wybraną opcję
choice = answers['choice'].lower()
print(f"You chose: {choice}")
