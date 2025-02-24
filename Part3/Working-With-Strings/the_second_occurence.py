string = input("Please type in a string: ")
substring = input("Please type in a substring: ")

index = 0
second_occurrence = False

while index + 3 <= len(string):
    if second_occurrence:
        print(f"The second occurrence of the substring is at index {index - 1}")
        break

    if string[index] == substring:
        second_occurrence = True

    index += 1
