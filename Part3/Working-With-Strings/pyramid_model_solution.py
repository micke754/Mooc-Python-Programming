n = int(input("Size: "))
row = "*"
while n > 0:
    print(f"{' ' * n + row}")
    row += "**"
    n -= 1
