﻿class Orange:
    def __init__(self, w, c):
        self.weight = w
        self.color = c
        print("Created!")


or1 = Orange(10, "black orange")
or1.weight = 100
or1.color = "light orange"

print(or1.weight)
print(or1.color)
