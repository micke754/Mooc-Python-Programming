hourly_wages = float(input("Hourly wage: "))
hours_worked = float(input("Hours worked: "))
day_of_the_week = input("Day of the week: ")

if day_of_the_week == "Sunday":
    print(f"Daily wages: {hourly_wages * 2 * hours_worked} euros")
else:
    print(f"Daily wages: {hourly_wages *  hours_worked} euros")
