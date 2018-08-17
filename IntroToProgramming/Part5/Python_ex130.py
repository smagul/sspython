colors = ["blue", "green", "orange"]
guess = input("Guess color: ")

if guess in colors:
    print("You guessed!")
else:
    print("Wrong! Try again.")
