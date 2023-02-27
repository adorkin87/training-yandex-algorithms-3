with open('input.txt', 'r') as f:
    source_array = f.readlines()
n, m = map(int, source_array[0].split())
matrix = []
for i in range(1, n+1):
    matrix.append(list(map(int, source_array[i].split())))
dp = [[]]
for j in range(m + 1):
    dp[0].append(0)
for i in range(1, n + 1):
    dp.append([])
    dp[i].append(0)
dp_map = [[]]
for i in range(1, n + 1):
    if i != 1:
        dp_map.append([])
    for j in range(1, m + 1):
        if i == j == 1:
            dp[i].append(matrix[i-1][j-1])
            dp_map[i-1].append(-1)
        else:
            if dp[i-1][j] >= dp[i][j-1]:
                dp[i].append(dp[i-1][j] + matrix[i-1][j-1])
                dp_map[i-1].append('D')
            else:
                dp[i].append(dp[i][j-1] + matrix[i-1][j-1])
                dp_map[i-1].append('R')
dp_exit = False
map = ''
pointer_i = n - 1
pointer_j = m - 1
if pointer_i == pointer_j == 0:
    pass
else:
    while dp_exit == False:
        map += dp_map[pointer_i][pointer_j]
        if dp_map[pointer_i][pointer_j] == 'D':
            pointer_i -= 1
        else:
            pointer_j -= 1
        if dp_map[pointer_i][pointer_j] == -1:
            dp_exit = True
print(dp[n][m])
print(map[::-1])
