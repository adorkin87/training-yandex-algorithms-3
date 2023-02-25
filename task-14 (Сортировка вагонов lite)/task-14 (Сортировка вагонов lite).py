class Stack:
    def __init__(self):
        self.stack = []

    def push(self, bracket):
        self.stack.append(bracket)

    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()

    def back(self):
        if len(self.stack) > 0:
            return (self.stack[-1])

    def size(self):
        return len(self.stack)


with open('./input.txt', 'r') as f:
    source_array = f.readlines()
n = int(source_array.pop(0))
wagons = (source_array[0]).split()
stack = Stack()
index = 1
for wagon in wagons:
    if int(wagon) != index:
        stack.push(wagon)
    else:
        stack.push(wagon)
        for i in range(stack.size()):
            if int(stack.back()) == index:
                stack.pop()
                index += 1
            else:
                break
if stack.size() != 0:
    print('NO')
else:
    print('YES')
