import random

def play_game(player_choice):
    choices = ['тас', 'қағаз', 'қайшы']
    computer_choice = random.choice(choices)
    
    print(f"Ойыншы таңдауы: {player_choice}")
    print(f"Компьютер таңдауы: {computer_choice}")
    
    if player_choice == computer_choice:
        return "Тең ойын!"
    elif (player_choice == 'тас' and computer_choice == 'қайшы') or \
         (player_choice == 'қағаз' and computer_choice == 'тас') or \
         (player_choice == 'қайшы' and computer_choice == 'қағаз'):
        return "Сіз жеңдіңіз!"
    else:
        return "Компьютер жеңді!"

# Тестілік сценарийлер
test_cases = ['тас', 'қағаз', 'қайшы']

for test in test_cases:
    result = play_game(test)
    print(f"Нәтиже: {result}\n")