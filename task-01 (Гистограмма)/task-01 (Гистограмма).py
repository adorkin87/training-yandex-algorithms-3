with open('./input.txt', 'r') as txt:
    source_str = txt.readlines()
str = ''.join(source_str)
clear_str = str.replace(' ', '')
clear_str = clear_str.replace('\n', '')
unique_set = set(clear_str)
unique_str = list(unique_set)
unique_str.sort()
dict_str = dict.fromkeys(unique_str)
max = 0
for symbol in dict_str.keys():
    count = clear_str.count(symbol)
    dict_str[symbol] = count
    if count > max:
        max = count
for i in range(max, 0, -1):
    result_str = ''
    for symbol in dict_str.keys():
        if dict_str.get(symbol) >= i:
            result_str += '#'
        else:
            result_str += ' '
    print(result_str)
result_str = ''
for i in dict_str.keys():
    result_str += i
print(result_str)
