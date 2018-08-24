qs = ["What's your name?",
      "What your favorite color?",
      "What are you doing?"]

n = 0
while True:
    print("Enter X for exit")
    a = input(qs[n])
    if a == "X":
        break
    n = (n + 1) % 3
