class Queue:
    def __init__(self):
        self.queue = []

    def push(self, n):
        self.queue.append(int(n))
        print('ok')

    def pop(self):
        if len(self.queue) > 0:
            print(self.queue.pop(0))
        else:
            print('error')

    def front(self):
        if len(self.queue) > 0:
            print(self.queue[0])
        else:
            print('error')

    def size(self):
        print(len(self.queue))

    def clear(self):
        self.queue.clear()
        print('ok')

    def exit(self):
        print('bye')


with open('./input.txt', 'r') as f:
    list_command = [_ for _ in f.readlines()]

queue = Queue()

for command in list_command:
    command = command.replace('\n', '')
    if command == 'pop':
        queue.pop()
    elif command == 'front':
        queue.front()
    elif command == 'size':
        queue.size()
    elif command == 'clear':
        queue.clear()
    elif command == 'exit':
        queue.exit()
        break
    else:
        queue.push(command.split(' ')[1])
