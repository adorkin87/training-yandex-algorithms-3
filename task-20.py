with open('input.txt', 'r') as f:
    source_array = f.readlines()
n = int(source_array.pop(0))
array = list(map(int, source_array[0].split()))
index = (n - 1) // 2
if (n - 1) % 2 == 1 and array[index] < array[(index * 2) + 1]:
    array[index], array[(index * 2) + 1] = array[(index * 2) + 1], array[index]
    index -= 1
for i in range(index + 1):
    current_index = index
    while current_index * 2 + 2 < n:
        max_child = current_index * 2 + 1
        if array[current_index * 2 + 2] > array[max_child]:
            max_child = current_index * 2 + 2
        if array[current_index] < array[max_child]:
            array[current_index], array[max_child] = array[max_child], array[current_index]
            current_index = max_child
        else:
            break
    index -= 1
for i in range(n):
    max_elem = array[0]
    array[0] = array[n - 1]
    index = 0
    while index * 2 + 2 < n:
        max_child = index * 2 + 1
        if array[index * 2 + 2] > array[max_child]:
            max_child = index * 2 + 2
        if array[index] < array[max_child]:
            array[index], array[max_child] = array[max_child], array[index]
            index = max_child
        else:
            break
    array[n - 1] = max_elem
    n -= 1
print(*array)
