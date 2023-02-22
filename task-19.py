class Heap:
    def __init__(self):
        self.heap = []

    def insert(self, n):
        self.heap.append(n)
        if len(self.heap) > 1:
            index = len(self.heap) - 1
            while index > 0 and self.heap[index] > self.heap[(index - 1) // 2]:
                self.heap[index], self.heap[(index - 1) // 2] = self.heap[(index - 1) // 2], self.heap[index]
                index = (index - 1) // 2

    def extract(self):
        result = self.heap[0]
        self.heap[0] = self.heap[- 1]
        index = 0
        while index * 2 + 2 < len(self.heap):
            max_child = index * 2 + 1
            if self.heap[index * 2 + 2] > self.heap[max_child]:
                max_child = index * 2 + 2
            if self.heap[index] < self.heap[max_child]:
                self.heap[index], self.heap[max_child] = self.heap[max_child], self.heap[index]
                index = max_child
            else:
                break
        self.heap.pop()
        print(result)


with open('input.txt', 'r') as f:
    list_command = f.readlines()
n = int(list_command.pop(0))

heap = Heap()

for command in list_command:
    command = command.replace('\n', '')
    if command == '1':
        heap.extract()
    else:
        heap.insert(int(command.split()[1]))
