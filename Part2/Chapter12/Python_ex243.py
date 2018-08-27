class Orange():
    def __init__(self, w, c):
        """weight in gramms"""
        self.weight = w
        self.color = c
        self.mold = 0
        print("Created!")

    def rot(self, days, temp):
        self.mold = days * temp


orange = Orange(6, "orange")
print(orange.mold)
orange.rot(10, 33)
print(orange.mold)

