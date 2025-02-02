sentence = ""
previous_word = ""

while True:
    word = input("Please type in a word: ")
    if word == "end":
        break
    if word == previous_word:
        break

    sentence += word + " "
    previous_word = word

print(sentence)
