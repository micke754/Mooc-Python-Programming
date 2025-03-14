number: int = int(input("Please type in a number: "))
lower: int = 1
upper: int = number
counter = 1

while counter <= number:
    if counter % 2 != 0:
        print(lower)
        counter += 1
        lower += 1
    else:
        print(upper)
        counter += 1
        upper -= 1
