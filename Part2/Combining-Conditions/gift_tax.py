gift_value = int(input("Value of gift: "))
tax = 0

if gift_value < 5_000:
    print("No tax!")
elif gift_value >= 5_000 and gift_value <= 25_000:
    print(f"Amount of tax: {100 + (gift_value - 5_000) * 0.08} euros")
elif gift_value > 25_000 and gift_value <= 55_000:
    print(f"Amount of tax: {1_700 + (gift_value - 25_000) * 0.10} euros")
elif gift_value > 55_000 and gift_value <= 200_000:
    print(f"Amount of tax: {4_700 + (gift_value - 55_000) * 0.12} euros")
elif gift_value > 200_000 and gift_value <= 1_000_000:
    print(f"Amount of tax: {22_100 + (gift_value - 200_000) * 0.15} euros")
elif gift_value > 1_000_000:
    print(f"Amount of tax: {142_100 + (gift_value - 1_000_000) * 0.17} euros")
