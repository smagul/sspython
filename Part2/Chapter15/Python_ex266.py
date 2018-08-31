class Card:
    suits = ["peaks", "worms", "bobi", "clubs"]

    values = [None, None, "2", "3",
              "4", "5", "6", "7",
              "8", "9", "10",
              "valeta", "damu",
              "queen", "tuza"]

    def __init__(self, v, s):
        """suit and value - integer numbers"""
        self.value = v
        self.suit = s

    def __lt__(self, c2):
        if self.value < c2.value:
            return True
        if self.value == c2.value and self.suit < c2.suit:
                return True
            
        return False

    def __gt__(self, c2):
        if self.value > c2.value:
            return True
        if self.value == c2.value and self.suit > c2.suit:
            return True

        return False

    def __repr__(self):
        v = self.values[self.value] + " of " \
            + self.suits[self.suit]
        return v
