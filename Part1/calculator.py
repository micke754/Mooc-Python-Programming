number1: int = int(input("Number 1: "))
number2: int = int(input("Number 2: "))
operation: str = input("Operation: ")

if operation == "add":
    print(f"{number1} + {number2} = {number1 + number2}")
elif operation == "subtract":
    print(f"{number1} - {number2} = {number1 - number2}")
elif operation == "multiply":
    print(f"{number1} * {number2} = {number1 * number2}")
