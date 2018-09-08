class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        try:
            return self.items[-1]
        except IndexError:
            return "List is empty"

    def size(self):
        return len(self.items)
