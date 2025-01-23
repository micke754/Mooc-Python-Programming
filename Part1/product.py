# number1: int = int(input("Please type in the first number:"))
# number2: int = int(input("Please type in the second number:"))
# number3: int = int(input("Please type in the third number:"))

# product = number1 * number2 * number3

# print(f"The product is {product}")

iterations: list[str] = ["First", "Second", "Third"]
numbers: list[int] = []

for iter in iterations:
    number: int = int(input(f"Please type in the {iter}:"))
    numbers.append(number)

result: int = 1

for i in numbers:
    result *= i

print(f"The product is {result}")
