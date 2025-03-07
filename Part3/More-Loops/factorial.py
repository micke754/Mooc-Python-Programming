while True:
    number = int(input("Please type in a number: "))

    factorial = 1
    counter = 1

    if number > 0:
        while counter <= number:
            factorial *= counter
            counter += 1
        print(f"The factorial of the number {number} is {factorial} ")
    else:
        break
print("Thanks and bye!")
