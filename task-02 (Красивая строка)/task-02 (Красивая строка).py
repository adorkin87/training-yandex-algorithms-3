with open ('input.txt', 'r') as f:
    source_array = f.readlines()
k = int(source_array[0])
stroka = source_array[1].rstrip()
set_unique_symbols = set(stroka)
result = 0
for unique_symbol in set_unique_symbols:
    pointer_1 = 0
    pointer_2 = 0
    k_current = k
    for current_symbol in stroka:
        if current_symbol == unique_symbol:
            pointer_2 += 1
            if result < pointer_2 - pointer_1:
                result = pointer_2 - pointer_1
        else:
            if k_current > 0:
                pointer_2 += 1
                k_current -= 1
                if result < pointer_2 - pointer_1:
                    result = pointer_2 - pointer_1
            else:
                pointer_current = pointer_2
                while pointer_current == pointer_2:
                    if stroka[pointer_1] == unique_symbol:
                        pointer_1 += 1
                    else:
                        pointer_1 += 1
                        if k_current < k and k_current < k:
                            k_current += 1
                    if k_current > 0:
                        pointer_2 += 1
                        k_current -= 1
print(result)
