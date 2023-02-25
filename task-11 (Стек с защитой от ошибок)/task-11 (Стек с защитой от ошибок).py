class Stack:
    def __init__(self):
        self.stack = []

    def push(self, n):
        self.stack.append(int(n))
        print('ok')

    def pop(self):
        if len(self.stack) > 0:
            print(self.stack.pop())
        else:
            print('error')

    def back(self):
        if len(self.stack) > 0:
            print(self.stack[-1])
        else:
            print('error')

    def size(self):
        print(len(self.stack))

    def clear(self):
        self.stack.clear()
        print('ok')

    def exit(self):
        print('bye')


with open('./input.txt', 'r') as f:
    list_command = [_ for _ in f.readlines()]

stack = Stack()

for command in list_command:
    command = command.replace('\n', '')
    if command == 'pop':
        stack.pop()
    elif command == 'back':
        stack.back()
    elif command == 'size':
        stack.size()
    elif command == 'clear':
        stack.clear()
    elif command == 'exit':
        stack.exit()
        break
    else:
        stack.push(command.split(' ')[1])
