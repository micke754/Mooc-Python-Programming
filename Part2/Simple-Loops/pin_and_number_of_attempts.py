attempt = 0
correct_pin = 4321
while True:
    pin = int(input("Pin: "))
    attempt += 1

    if attempt == 1 and pin == correct_pin:
        print("Correct! It only took you one single attempt!")
        break

    elif pin == correct_pin:
        print(f"Correct! It took you {attempt} attempts")
        break
    else:
        print("Wrong")
