class Shape():
    def __init(self, w, l):
        self.width = w
        self.len = l

    def print_size(self):
        print("""{} na {}""".format(self.width, self.len))


class Square(Shape):
    pass


a_square = Square(20, 20)
a_square.print_size()
