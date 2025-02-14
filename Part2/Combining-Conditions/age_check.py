age = int(input("What is your age?"))
text = input("What is your age?")

number = 0

if age > 4:
    print(f"Ok, you're {age} years old")
elif age < 4 and age >= 0:
    print("I suspect you can't write quite yet...")
elif age < 0:
    print("That must be a mistake")
