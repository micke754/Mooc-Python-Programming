word = input("Word: ")

if len(word) % 2 == 0:
    left_mult = int((28 - len(word)) / 2) - 1
    right_mult = int((28 - len(word)) / 2)
else:
    left_mult = int((28 - len(word)) / 2)
    right_mult = int((28 - len(word)) / 2)

print("*" * 30)
print(f"* {' ' * left_mult}{word}{' ' * right_mult}*")
print("*" * 30)
