input_year = int(input("Year: "))

year = input_year + 1

while True:
    if year % 100 == 0:
        if year % 400 == 0:
            break
    elif year % 4 == 0:
        break
    year += 1

print(f"The next leap year after {input_year} is {year}")
