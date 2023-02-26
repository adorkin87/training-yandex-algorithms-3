with open('input.txt', 'r') as f:
    source_array = f.readlines()
sectors = int(source_array.pop(0))
os = int(source_array.pop(0))
parts = []
for i in range(os):
    p_s, p_e = map(int, source_array.pop(0).split())
    if len(parts) == 0:
        parts.append((p_s, p_e))
    else:
        parts_del = []
        for j in range(len(parts)):
            if p_s <= parts[j][0] <= p_e or p_s <= parts[j][1] <= p_e or parts[j][0] <= p_e <= parts[j][1]:
                parts_del.append(parts[j])
        if len(parts_del) > 0:
            for j in range(len(parts_del)):
                parts.remove(parts_del[j])
        parts.append((p_s, p_e))
print(len(parts))
