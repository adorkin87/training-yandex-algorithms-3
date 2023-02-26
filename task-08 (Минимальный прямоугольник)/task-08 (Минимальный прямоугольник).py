with open('input.txt', 'r') as f:
    source_array = f.readlines()
k = int(source_array.pop(0))
set_x = set()
set_y = set()
for i in range(k):
    x, y = map(int, source_array.pop(0).split())
    set_x.add(x)
    set_y.add(y)
print(min(set_x), min(set_y), max(set_x), max(set_y))
