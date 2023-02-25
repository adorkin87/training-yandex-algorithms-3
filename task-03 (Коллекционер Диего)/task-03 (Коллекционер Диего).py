n = input()
list_n = list({int(i) for i in input().split(' ')})
k = input()
list_k = [int(i) for i in input().split(' ')]
list_n.sort()

for i in list_k:

    result = 0
    start = 0
    end = len(list_n) - 1
    middle_index = end // 2

    if i > list_n[end]:
        result = end + 1
    elif i < list_n[start]:
        result = 0
    elif i == list_n[middle_index]:
        result = middle_index
    else:
        while start <= end:
            if i > list_n[middle_index]:
                start = middle_index + 1
            else:
                end = middle_index - 1
            middle_index = (start + end) // 2
        result = middle_index + 1
    print(result)
