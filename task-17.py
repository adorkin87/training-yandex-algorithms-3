with open('input.txt', 'r') as f:
    source_array = f.readlines()
first_gamer = list(map(int, source_array[0].split()))
second_gamer = list(map(int, source_array[1].split()))
count = 0
while len(first_gamer) != 0 and len(second_gamer) != 0:
    if first_gamer[0] in [0, 9] and second_gamer[0] in [0, 9]:
        if first_gamer[0] > second_gamer[0]:
            second_gamer.append(first_gamer.pop(0))
            second_gamer.append(second_gamer.pop(0))
        else:
            first_gamer.append(first_gamer.pop(0))
            first_gamer.append(second_gamer.pop(0))
    elif first_gamer[0] > second_gamer[0]:
        first_gamer.append(first_gamer.pop(0))
        first_gamer.append(second_gamer.pop(0))
    else:
        second_gamer.append(first_gamer.pop(0))
        second_gamer.append(second_gamer.pop(0))
    count += 1
result = ''
if len(first_gamer) == 0:
    result += 'second'
else:
    result += 'first'
print(result + ' ' + str(count))
