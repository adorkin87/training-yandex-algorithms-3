with open('./input.txt', 'r') as f:
    source_array = [int(_) for _ in f.readlines()]
count_students = source_array.pop(0)
count_var = source_array.pop(0)
petr_desk = source_array.pop(0)
petr_position = source_array.pop(0)

count_desk = count_students // 2 if count_students % 2 == 0 else count_students // 2 + 1
petr_list_number = petr_desk * 2 - 1 if petr_position == 1 else petr_desk * 2
if count_var >= petr_list_number:
    petr_var = petr_list_number
else:
    petr_var = count_var if petr_list_number % count_var == 0 else petr_list_number % count_var
j = petr_list_number // count_var
desk_top = -1
desk_bottom = -1

if petr_list_number // count_var >= 1:
    if petr_list_number // count_var == 1 and petr_list_number % count_var != 0:
        desk_bottom = petr_list_number - count_var if petr_list_number % count_var == 1 else (petr_list_number - count_var) // 2
        position_result_bottom = 2 if (petr_list_number - count_var) % 2 == 0 else 1
    elif petr_list_number // count_var > 1:
        desk_bottom = (petr_list_number - count_var) // 2 if (petr_list_number - count_var) % 2 == 0 else ((petr_list_number - count_var) // 2) + 1
        position_result_bottom = 2 if (petr_list_number - count_var) % 2 == 0 else 1

if (petr_list_number + count_var) // 2 < count_desk:
    desk_top = (petr_list_number + count_var) // 2 if (petr_list_number + count_var) % 2 == 0 else ((petr_list_number + count_var) // 2) + 1
    position_result_top = 2 if (petr_list_number + count_var) % 2 == 0 else 1
elif (petr_list_number + count_var) // 2 == count_desk:
    if (petr_list_number + count_var) % 2 == 0 and count_students % 2 == 0:
        desk_top = count_desk
        position_result_top = 2

if desk_top == -1 and desk_bottom == -1:
    print('-1')
elif desk_top == -1:
    print(desk_bottom, position_result_bottom)
elif desk_bottom == -1:
    print(desk_top, position_result_top)
else:
    if desk_top - petr_desk <= petr_desk - desk_bottom:
        print(desk_top, position_result_top)
    else:
        print(desk_bottom, position_result_bottom)
