points_on_card = int(input("How many points are on your card? "))

if points_on_card < 100:
    total_points = points_on_card + (points_on_card * 0.1)
    print("Your bonus is 10%")
else:
    total_points = points_on_card + (points_on_card * 0.15)
    print("Your bonus is 15%")

print(f"You now have {total_points} points")
