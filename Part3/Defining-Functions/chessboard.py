def chessboard(n: int):
    for i in range(n):
        text = ""
        if i % 2 == 0:
            for i in range(n):
                if i % 2 == 0:
                    text += "1"
                else:
                    text += "0"
        else:
            for i in range(n):
                if i % 2 == 0:
                    text += "0"
                else:
                    text += "1"
        print(text)


def chessboard_model(n: int):
    counter = 0
    while counter < n:
        if counter % 2 == 0:
            row = "10" * n
        else:
            row = "01" * n
        print(row[:n])
        counter += 1


if __name__ == "__main__":
    chessboard(3)
    print("\nModel Solution")
    chessboard_model(3)
    print("\n")
    chessboard(6)
    print("\nModel Solution")
    chessboard_model(6)
