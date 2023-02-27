with open('input.txt', 'r') as f:
    stroka = f.readline().rstrip()
set_symbols = set(stroka)
dict_symbols = dict.fromkeys(set_symbols, 0)
for i in range(len(stroka)):
    if i == 0:
        dict_symbols[stroka[i]] += len(stroka)
    elif i == len(stroka) - 1:
        dict_symbols[stroka[i]] += len(stroka)
    else:
        dict_symbols[stroka[i]] += (i+1) * (len(stroka) - i)
sorted_list = sorted(dict_symbols.items())
for i in range(len(sorted_list)):
    print(str(sorted_list[i][0]) + ': ' + str(sorted_list[i][1]))
