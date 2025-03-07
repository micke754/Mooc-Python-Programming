number = int(input("Please type in a number: "))


if number >= 0:
    operand_1 = 1
    while operand_1 <= number:
        operand_2 = 1
        while operand_2 <= number:
            print(f"{operand_1} x {operand_2} = {operand_1 * operand_2}")
            operand_2 += 1
        operand_1 += 1
