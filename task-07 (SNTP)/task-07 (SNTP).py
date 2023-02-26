with open('input.txt', 'r') as f:
    source_array = f.readlines()
a_hh, a_mm, a_ss = map(int, source_array.pop(0).split(':'))
b_hh, b_mm, b_ss = map(int, source_array.pop(0).split(':'))
c_hh, c_mm, c_ss = map(int, source_array.pop(0).split(':'))
convert_a_ss = (a_hh * 60 + a_mm) * 60 + a_ss
convert_b_ss = (b_hh * 60 + b_mm) * 60 + b_ss
convert_c_ss = (c_hh * 60 + c_mm) * 60 + c_ss
get_time = convert_c_ss - convert_a_ss
if get_time >= 0:
    if get_time % 2 == 0:
        result_ss = convert_b_ss + get_time // 2
    else:
        result_ss = convert_b_ss + get_time // 2 + 1
else:
    get_time = (24 * 60 * 60 - convert_a_ss) + convert_c_ss
    if get_time % 2 == 0:
        result_ss = convert_b_ss + get_time // 2
    else:
        result_ss = convert_b_ss + get_time // 2 + 1
result_hh = (result_ss // 60) // 60
if result_hh >= 24:
    result_hh -= 24
result_mm = (result_ss // 60) % 60
result_ss = result_ss % 60
result_str = str(result_hh) + ':' if result_hh >= 10 else '0' + str(result_hh) + ':'
result_str += str(result_mm) + ':' if result_mm >= 10 else '0' + str(result_mm) + ':'
result_str += str(result_ss) if result_ss >= 10 else '0' + str(result_ss)
print(result_str)
