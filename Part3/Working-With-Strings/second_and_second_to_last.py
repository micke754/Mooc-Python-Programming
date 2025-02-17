message = input("Please type in a string: ")

if message[1] == message[-2]:
    print(f"The second and the second to last characters are {message[1]}")
elif message[1] != message[-2]:
    print("The second and the second to last characters are different")
