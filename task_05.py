def good_str(str: list, row: int) -> int:
    result = 0
    start = 0
    count = 0
    for index in str:
        if str[index] >= row:
            count += 1
        else:
            if count > 1:
                result += count - start - 1
            start = 0
            count = 0
    if count > 1:
        result += count - start - 1
    return result

with open('input.txt', 'r') as f:
    array_source = [int(_) for _ in f.readlines()]
n = array_source.pop(0)
max = max(array_source)
min = min(array_source)
result = min * (n - 1)
for row in range(min + 1, max + 1):
    start = 0
    count = 0
    for index in range(n):
        if array_source[index] >= row:
            count += 1
        else:
            if count > 1:
                result += (count - start - 1)
            start = 0
            count = 0
    if count > 1:
        result += (count - start - 1)
print(result)
