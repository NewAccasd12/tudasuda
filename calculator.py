class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Нөлге бөлуге болмайды")
        return a / b

def main():
    calc = Calculator()
    
    while True:
        print("\nҚарапайым калькулятор")
        print("1. +")
        print("2. -")
        print("3. *")
        print("4. /")
        print("5. Шығу")
        
        choice = input("Операцияны таңдаңыз (1-5): ")
        
        if choice == '5':
            print("Бағдарлама аяқталды.")
            break
        
        if choice not in {'1', '2', '3', '4'}:
            print("Қате! Дұрыс операция таңдаңыз.")
            continue

        try:
            num1 = float(input("Бірінші санды енгізіңіз: "))
            num2 = float(input("Екінші санды енгізіңіз: "))

            if choice == '1':
                print(f"Нәтиже: {calc.add(num1, num2)}")
            elif choice == '2':
                print(f"Нәтиже: {calc.subtract(num1, num2)}")
            elif choice == '3':
                print(f"Нәтиже: {calc.multiply(num1, num2)}")
            elif choice == '4':
                print(f"Нәтиже: {calc.divide(num1, num2)}")

        except ValueError:
            print("Қате! Сан енгізіңіз.")

if __name__ == "__main__":
    main()
