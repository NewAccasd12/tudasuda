import time

def normalize_text(text):
    return text.strip().lower().replace("!", "").replace(".", "").replace(",", "")

def speed_typing_game(typed_text, start_time):
    text = "Python - бұл керемет бағдарламалау тілі!"
    
    end_time = time.time()
    time_taken = end_time - start_time
    
    if normalize_text(typed_text) == normalize_text(text):
        result = "Құттықтаймын! Сіз мәтінді дұрыс жаздыңыз!"
    else:
        result = "Мәтінде қателер бар!"
    
    words = len(text.split())
    wpm = (words / time_taken) * 60  # Сөз/минут есебі

    return f"{result}\nСіз {time_taken:.2f} секундта жазып бітірдіңіз. Жылдамдығыңыз: {wpm:.2f} сөз/мин."

# Тестілік сценарийлер
test_cases = [
    "Python - бұл керемет бағдарламалау тілі!",  # Дұрыс
    "python - бұл керемет бағдарламалау тілі!",  # Регистрді елемеу
    "Python - бұл керемет бағдарламалау тілі",   # Нүктесіз
    "Python - керемет!",                         # Толық емес мәтін
    ""                                           # Бос енгізу
]

for test in test_cases:
    start_time = time.time()
    time.sleep(1)  # Уақыттың нақтырақ есептелуі үшін кідіріс
    result = speed_typing_game(test, start_time)
    print(f"Тексеру: {test}\nНәтиже: {result}\n")