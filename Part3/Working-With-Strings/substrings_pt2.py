message = input("Please type in a string: ")

reversed_message = message[::-1]

counter = len(message)

while counter >= 0:
    print(message[counter::])
    counter -= 1
