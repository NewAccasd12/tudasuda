import math

# Функция для вычисления площади круга
def circle_area(radius):
    return math.pi * radius ** 2

# Тестовые данные
test_cases = [
    (1, math.pi),  # радиус 1, площадь = π
    (2, 4 * math.pi),  # радиус 2, площадь = 4π
    (5, 25 * math.pi),  # радиус 5, площадь = 25π
]

# Тестирование
for radius, expected in test_cases:
    result = circle_area(radius)
    assert abs(result - expected) < 0.0001, f"Ошибка: для радиуса {radius} ожидалось {expected}, но получилось {result}"

print("Все тесты прошли успешно!")



