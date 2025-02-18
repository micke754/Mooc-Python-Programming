message = input("Please type in a word: ")
character = input("Please type in a character: ")
start_position = message.find(character)
substring_length = len(message[start_position : start_position + 3])

if substring_length == 3:
    if character in message:
        print(message[start_position : start_position + 3])
