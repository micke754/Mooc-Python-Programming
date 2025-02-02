input_year = int(input("Year: "))


def calculate_next_leap_year(input_year: int, next_leap_year: int = 0) -> int:
    next_leap_year = 4 - (input_year % 4) + input_year
    if is_not_leap_year(next_leap_year):
        next_leap_year += 4

    return next_leap_year


def is_not_leap_year(year: int, input_is_leap_year=True) -> bool:
    if year % 100 == 0:
        if year % 400 == 0:
            input_is_leap_year = False
        else:
            input_is_leap_year = True
    else:
        if year % 4 == 0:
            input_is_leap_year = False
        else:
            input_is_leap_year = True
    return input_is_leap_year


next_leap_year = calculate_next_leap_year(input_year)

print(
    f"The input year {input_year} was not a leap year: {is_not_leap_year(input_year)}"
)

print(f"The next leap year after {input_year} is {next_leap_year}")
