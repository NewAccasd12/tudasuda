import random

def hangman():
    words = ["python", "java", "javascript", "ruby", "html", "css"]
    word = random.choice(words)
    guessed = "_" * len(word)
    attempts = 6
    guessed_letters = []

    print("Добро пожаловать в игру 'Виселица'!")

    while attempts > 0 and "_" in guessed:
        print(f"Слово: {guessed}")
        print(f"Попыток осталось: {attempts}")
        print(f"Использованные буквы: {', '.join(guessed_letters)}")
        
        letter = input("Введите букву: ").lower()
        
        if letter in guessed_letters:
            print("Вы уже угадывали эту букву.")
            continue

        if letter in word:
            guessed_letters.append(letter)
            guessed = "".join([letter if word[i] == letter else guessed[i] for i in range(len(word))])
        else:
            guessed_letters.append(letter)
            attempts -= 1

    if "_" not in guessed:
        print(f"Поздравляю! Вы угадали слово: {word}")
    else:
        print(f"Вы проиграли. Загаданное слово было: {word}")

hangman()