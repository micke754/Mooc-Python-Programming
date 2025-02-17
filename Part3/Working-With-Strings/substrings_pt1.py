message = input("Please type in a string: ")

message[:1]

counter = 1
while counter <= len(message):
    print(message[:counter])
    counter += 1
