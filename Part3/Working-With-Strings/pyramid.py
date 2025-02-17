limit = int(input("Limit: "))
stars = 1
while limit >= 0:
    print(f"{' ' * limit} {'*' * stars}")
    limit -= 1
    stars += 2
