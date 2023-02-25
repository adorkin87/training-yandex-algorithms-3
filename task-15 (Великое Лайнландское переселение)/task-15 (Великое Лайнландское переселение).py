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
cities = list(map(int, source_array[0].split()))
stack = Stack()
stack.push((cities[0], 0))
for i in range(1, n):
    if cities[i] >= stack.back()[0]:
        stack.push((cities[i], i))
    else:
        for j in range(stack.size()):
            if cities[i] < stack.back()[0]:
                cities[stack.pop()[1]] = i
            else:
                break
        stack.push((cities[i], i))
for i in range(stack.size()):
    cities[stack.pop()[1]] = -1
result = ' '.join(map(str, cities))
print(result)
