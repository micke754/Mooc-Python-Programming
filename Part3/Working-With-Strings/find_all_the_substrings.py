message = input("Please type in a message: ")
character = input("Please type in a character: ")

start_position = message.find(character)


while message:
    substring = message[start_position : start_position + 3]
    if len(substring) < 3:
        break
    if character in message:
        print(substring)
    message = message[start_position + 1 : :]
    start_position = message.find(character)
