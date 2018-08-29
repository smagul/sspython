﻿class Shape():
    def __init__(self, w, l):
        self.width = w
        self.len = l

    def print_size(self):
        print("""{} na {}""".format(self.width, self.len))


class Square(Shape):
    def area(self):
        return self.width * self.len


a_square = Square(20, 20)
print(a_square.area())
