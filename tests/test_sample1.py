# calculator.py
def calculator(num1, operation, num2):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        if num2 == 0:
            raise ValueError("Нөлге бөлу мүмкін емес!")
        return num1 / num2
    else:
        raise ValueError("Қате: Белгісіз операция.")
