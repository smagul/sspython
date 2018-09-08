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
            return "Stack is empty."

    def size(self):
        return len(self.items)


stack = Stack()
for c in "Hello":
    stack.push(c)

reverse = ""

for _ in range(stack.size()):
    reverse += stack.pop()

print(reverse)