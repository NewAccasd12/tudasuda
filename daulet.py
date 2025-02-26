import random

def guess_the_number():
    print("Угадай число от 1 до 100!")
    
    # Загадать число
    number_to_guess = random.randint(1, 100)
    
    # Число попыток
    attempts = 0

    while True:
        try:
            # Получаем ввод от пользователя
            user_guess = int(input("Введите число: "))
            attempts += 1

            # Проверка на правильность
            if user_guess < number_to_guess:
                print("Слишком маленькое число!")
            elif user_guess > number_to_guess:
                print("Слишком большое число!")
            else:
                print(f"Поздравляю! {number_to_guess} за {attempts} попыток.")
                break
        except ValueError:
            print("Только числа!")

# Запуск игры
guess_the_number()
