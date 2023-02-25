class Queue:
    def __init__(self):
        self.queue = []

    def push_front(self, n):
        self.queue.insert(0, int(n))
        print('ok')
    def push_back(self, n):
        self.queue.append(int(n))
        print('ok')

    def pop_front(self):
        if len(self.queue) > 0:
            print(self.queue.pop(0))
        else:
            print('error')

    def pop_back(self):
        if len(self.queue) > 0:
            print(self.queue.pop())
        else:
            print('error')

    def front(self):
        if len(self.queue) > 0:
            print(self.queue[0])
        else:
            print('error')

    def back(self):
        if len(self.queue) > 0:
            print(self.queue[-1])
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
    if 'push' in command:
        command, value = command.split()
    if command == 'pop_front':
        queue.pop_front()
    elif command == 'pop_back':
        queue.pop_back()
    elif command == 'front':
        queue.front()
    elif command == 'back':
        queue.back()
    elif command == 'size':
        queue.size()
    elif command == 'clear':
        queue.clear()
    elif command == 'exit':
        queue.exit()
        break
    elif command == 'push_front':
        queue.push_front(value)
    elif command == 'push_back':
        queue.push_back(value)
