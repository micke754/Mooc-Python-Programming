def squared(text: str, n: int):
    counter = 0
    text_large = text * (n**2)
    moving_index = 0
    index = 0
    while counter < n:
        if counter == 0:
            index = 0
        else:
            index = moving_index
        row = text_large[index : index + n]
        print(row)
        counter += 1
        moving_index += n


if __name__ == "__main__":
    print("\nTest 1")
    squared("ab", 3)
    print("\nTest 2")
    squared("aybabtu", 5)
