class Game:
    def __init__(self):
        name1 = input("Name of player 1: ")
        name2 = input("Name of player 2: ")
        self.deck = Deck()
        self.p1 = Player(name1)
        self.p2 = Player(name2)

    def wins(self, winner):
        print("{} zabiraet karty".format(winner))

    def draw(self, p1n, p1c, p2n, p2c):
        d = "{} kladet {}, a {} kladet {}"
        d = d.format(p1n, p1c, p2n, p2c)
        print(d)

    def play_game(self):
        cards = self.deck.cards
        print("Go!")
        while len(cards) >= 2:
            m = "Enter X for exit. Enter any key for start the game. "
            response = input(m)
            if response == 'X':
                break
            p1c = self.deck.rm_card()
            p2c = self.deck.rm_card()
            p1n = self.p1.name
            p2n = self.p2.name
            self.draw(p1n, p1c, p2n, p2c)
            if p1c > p2c:
                self.p1.wins += 1
                self.wins(self.p1.name)
            else:
                self.p2.wins += 1
                self.wins(self.p2.name)

        win = self.winner(self.p1, self.p2)

        print("Game over. {} win!".format(win))

    def winner(self, p1, p2):
        if p1.wins > p2.wins:
            return p1.name
        if p1.wins < p2.wins:
            return p2.name
        return "Draw!"
