while wrong < len(stages) - 1:
    print("\n")
    msg = "Enter the letter: "
    char = input(msg)
    if char in rletters:
        cind = rletters.index(char)
        board[cind] = char
        rletters[cind] = '$'
    else:
        wrong += 1
    print((" ".join(board)))
    e = wrong + 1
    print("\n".join(stages[0:e]))
    if "__" not in board:
        print("You win! Was word: ")
        print(" ".join(board))
        win = True
        break
