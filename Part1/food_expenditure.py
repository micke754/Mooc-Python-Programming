cafeteria_frequency: int = int(
    input("How many times a week do you eat at the student cafeteria? ")
)

price_of_lunch: float = float(input("The price of a typical student lunch? "))

price_of_groceries: float = float(
    input("How much money do you spend on groceries in a week? ")
)

mean_weekly_food_expense: float = (
    price_of_lunch * cafeteria_frequency + price_of_groceries
)

mean_daily_food_expense: float = mean_weekly_food_expense / 7

print(
    f"Average food expenditure \nDaily: {mean_daily_food_expense} euros\nWeekly: {mean_weekly_food_expense} euros"
)
