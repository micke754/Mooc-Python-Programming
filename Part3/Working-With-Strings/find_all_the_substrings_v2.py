string = input("Please type in a string: ")
substring = input("Please type in a substring: ")

if not substring:
    print("The substring cannot be empty.")
else:
    counter = 0
    index = 0
    # Ensure we only iterate while there's enough room for a match
    while index <= len(string) - len(substring):
        if string[index : index + len(substring)] == substring:
            counter += 1
            if counter == 2:
                print(f"The second occurrence of the substring is at index {index}.")
                break
            # Jump past this occurrence to avoid overlapping
            index += len(substring)
        else:
            index += 1

    if counter < 2:
        print("The substring does not occur twice in the string.")
