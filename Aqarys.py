import time

def speed_typing_game():
    print("Кім жылдам? Ойынына қош келдіңіз!")
    print("Төмендегі мәтінді тез және қатесіз жазып көріңіз.")

    text = "Python - бұл керемет бағдарламалау тілі!"
    print("\nМәтін:")
    print(text)

    input("\nОйынды бастау үшін Enter басыңыз...")

    start_time = time.time()  # Ойын басталған уақыт
    typed_text = input("Мәтінді жазып көріңіз: ")

    end_time = time.time()  # Ойын аяқталған уақыт
    time_taken = end_time - start_time

    if typed_text == text:
        print(f"\nҚұттықтаймын! Сіз мәтінді дұрыс жаздыңыз!")
    else:
        print("\nМәтінде қателер бар!")

    print(f"Сіз {time_taken:.2f} секундта жазып бітірдіңіз.")

speed_typing_game()