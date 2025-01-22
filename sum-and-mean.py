number_of_iterations: int = 4
numbers: list[int] = []

for i in range(number_of_iterations):
    number: int = int(input(f"Number {i + 1}: "))
    numbers.append(number)

sum: int = 0

for number in numbers:
    sum += number

mean: float = sum / number_of_iterations

print(f"The sum of the numbers: {sum} and the mean is {mean}")
