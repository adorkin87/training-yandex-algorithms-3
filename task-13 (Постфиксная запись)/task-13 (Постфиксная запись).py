class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()

    def back(self):
        if len(self.stack) > 0:
            return self.stack[-1]

    def size(self):
        return len(self.stack)


with open('input.txt', 'r') as f:
    line = f.readline()
array_data = line.split()
stack = Stack()
operators = {'+', '-', '*', '/'}
for symbol in array_data:
    if symbol in operators:
        num1 = stack.pop()
        num2 = stack.pop()
        stack.push(str(eval(num2 + symbol + num1)))
    else:
        stack.push(symbol)
print(stack.back())
