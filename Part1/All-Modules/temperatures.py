temperature_f: int = int(input("Please type in a temperature(F):"))
temperature_c: float = (temperature_f - 32) * 5 / 9

if temperature_c < 0:
    print(f"{temperature_f} degrees Fahrenheit equals {temperature_c} degrees Celsius")
    print("Brr! It's cold in here!")
else:
    print(f"{temperature_f} degrees Fahrenheit equals {temperature_c} degrees Celsius")
