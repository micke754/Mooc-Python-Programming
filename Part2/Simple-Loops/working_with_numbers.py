numbers: str = ""
sum = 0
positive_count: int = 0
negative_count = 0
print("Please type in integer numbers. Type in 0 to finish.")
while True:
    number = int(input("Number: "))

    if number == 0:
        break

    if number < 0:
        negative_count += 1
    else:
        positive_count += 1

    numbers += str(number) + " "
    sum += number

count = len(numbers.split())
mean = sum / count
print("...the program asks for numbers")
print(f"Numbers typed in {count}")
print(f"The sum of the numbers is {sum}")
print(f"The mean of the numbers is {mean}")
print(f"Positive numbers {positive_count}")
print(f"Negative numbers {negative_count}")
