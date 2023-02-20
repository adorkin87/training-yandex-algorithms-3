def good_str(str: list, row: int) -> int:
    result = 0
    start = 0
    count = 0
    for number in str:
        if number >= row:
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
sort_index_array = sorted(array_source)
previous_index = 0
result = 0
for index_row in sort_index_array:
    result += (index_row - previous_index) * good_str(array_source, index_row)
    previous_index = index_row
print(result)
