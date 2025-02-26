import pytest
from io import StringIO
from unittest.mock import patch

# Ваш код игры будет импортироваться, например:
# from guess_number import guess_number


def test_guess_number_correct_guess():
    with patch('random.randint', return_value=50):  # Принудительно задаем загаданное число
        with patch('builtins.input', return_value="50"):  # Подставляем правильный ответ пользователя
            with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                guess_number()
                output = mock_stdout.getvalue()
                assert "Поздравляем! Вы угадали число 50" in output


def test_guess_number_incorrect_guess():
    with patch('random.randint', return_value=50):  # Загаданное число 50
        with patch('builtins.input', side_effect=["40", "60", "50"]):  # Первый неправильный, второй тоже неправильный
            with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                guess_number()
                output = mock_stdout.getvalue()
                assert "Слишком маленькое число!" in output
                assert "Слишком большое число!" in output
                assert "Поздравляем! Вы угадали число 50" in output


def test_invalid_input():
    with patch('random.randint', return_value=50):  # Загаданное число 50
        with patch('builtins.input', side_effect=["abc", "50"]):  # Некорректный ввод сначала
            with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                guess_number()
                output = mock_stdout.getvalue()
                assert "Пожалуйста, введите целое число." in output
                assert "Поздравляем! Вы угадали число 50" in output
