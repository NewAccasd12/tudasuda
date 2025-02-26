import random

def guess_number():
    print("Добро пожаловать в игру 'Угадай число'!")
    print("Я загадал число от 1 до 100. Попробуй его угадать.")
    
    # Генерируем случайное число от 1 до 100
    number_to_guess = random.randint(1, 100)
    
    attempts = 0  # Счётчик попыток
    
    while True:
        # Получаем число от игрока
        try:
            player_guess = int(input("Введите ваше число: "))
        except ValueError:
            print("Пожалуйста, введите целое число.")
            continue
        
        attempts += 1
        
        # Проверяем, угадал ли игрок
        if player_guess < number_to_guess:
            print("Слишком маленькое число! Попробуйте снова.")
        elif player_guess > number_to_guess:
            print("Слишком большое число! Попробуйте снова.")
        else:
            print(f"Поздравляем! Вы угадали число {number_to_guess} за {attempts} попыток.")
            break

# Запуск игры
guess_number()