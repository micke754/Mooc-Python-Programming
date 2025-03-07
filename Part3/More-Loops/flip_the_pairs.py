number = int(input("Please type in a number: "))

counter = 1

if number == 1:
    print(counter)
else:
    while counter <= number:
        if counter == number and counter % 2 != 0:
            print(counter)
            break
        if counter % 2 == 0:
            print(counter)
            print(counter - 1)

        counter += 1
