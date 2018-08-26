rhymes = {"1": "laugh",
          "2": "blue",
          "3": "I",
          "4": "floor",
          "5": "life"
}

n = input("Enter the number: ")
if n in rhymes:
    rhyme = rhymes[n]
    print(rhyme)
else:
    print("Not found.")
