def calculator():
    num1 = float(input("Бірінші санды енгізіңіз: "))
    operation = input("Операцияны таңдаңыз (+, -, *, /): ")
    num2 = float(input("Екінші санды енгізіңіз: "))
    
    if operation == "+":
        print(f"Нәтиже: {num1 + num2}")
    elif operation == "-":
        print(f"Нәтиже: {num1 - num2}")
    elif operation == "*":
        print(f"Нәтиже: {num1 * num2}")
    elif operation == "/":
        if num2 == 0:
            print("Нөлге бөлу мүмкін емес!")
        else:
            print(f"Нәтиже: {num1 / num2}")
    else:
        print("Қате: Белгісіз операция.")

calculator()