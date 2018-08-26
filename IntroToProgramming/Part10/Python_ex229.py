def hangman(word):
    wrong = 0
    stages = ["",
             "_ _____ _             ",
             "|                     ",
             "|           |         ",
             "|           O         ",
             "|          /|\        ",
             "|          / \        ",
             "|                     "
             ]
    rletters = list(word)
    board = ["__"] * len(word)
    win = False
    print("Welcome to hang!")
