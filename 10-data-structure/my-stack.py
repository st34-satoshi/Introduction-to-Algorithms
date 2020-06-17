class MyStack:

    def __init__(self):
        self.stack = []

    def empty(self):
        return len(self.stack) == 0

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        return self.stack.pop()

    def print(self):
        print(self.stack)


if __name__ == '__main__':
    stack = MyStack()
    stack.push(1)
    stack.push(2)
    stack.print()
    stack.pop()
    stack.print()
