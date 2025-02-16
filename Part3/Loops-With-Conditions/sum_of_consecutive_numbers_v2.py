limit = int(input("Limit: "))
counter = 1
sum = 0
message = "The consecutive sum: 1"

while sum < limit:
    sum += counter

    if sum >= limit:
        message += f" = {sum}"
    else:
        message += f" + {counter + 1}"
    counter += 1


print(message)
