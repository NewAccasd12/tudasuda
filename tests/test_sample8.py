import random

def choose_word():
    words = ["python", "computer", "hangman", "programming", "kazakhstan"]
    return random.choice(words)

def display(word, guessed_letters):
    return " ".join(letter if letter in guessed_letters else "_" for letter in word)

def hangman():
    word = choose_word()
    guessed_letters = set()
    attempts = 6
    
    print("Добро пожаловать в игру Виселица!")
    
    while attempts > 0:
        print("\nСлово:", display(word, guessed_letters))
        print(f"Осталось попыток: {attempts}")
        guess = input("Введите букву: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Пожалуйста, введите одну букву.")
            continue
        
        if guess in guessed_letters:
            print("Вы уже угадали эту букву!")
            continue
        
        guessed_letters.add(guess)
        
        if guess not in word:
            attempts -= 1
            print("Неправильно!")
        
        if all(letter in guessed_letters for letter in word):
            print("Поздравляем! Вы угадали слово:", word)
            return
    
    print("Вы проиграли! Загаданное слово было:", word)

if __name__ == "__main__":
    hangman()
