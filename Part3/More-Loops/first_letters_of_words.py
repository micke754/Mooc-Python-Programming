sentence = input("Please type in a sentence: ")

# sentence = "Humpty Dumpty sat on a wall"

words = sentence.split()


if sentence:
    number_of_words = len(words)
    index = 0
    while index < number_of_words:
        print(words[index][0])
        index += 1
