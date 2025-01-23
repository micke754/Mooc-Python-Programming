number_of_iterations: int = 2
numbers: list[int] = []

for i in range(number_of_iterations):
    number: int = int(input(f"Number {i + 1}: "))
    numbers.append(number)

product: int = 1
sum: int = 0

for number in numbers:
    sum += number
    product *= number

print(f"The sum of the numbers: {sum}")
print(f"The product of the numbers: {product}")
