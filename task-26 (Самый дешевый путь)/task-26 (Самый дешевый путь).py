with open('input.txt', 'r') as f:
    source_array = f.readlines()
n, m = map(int, source_array[0].split())
matrix = []
for i in range(1, n+1):
    matrix.append(list(map(int, source_array[i].split())))
dp = [[]]
for j in range(m + 1):
    dp[0].append(float('inf'))
for i in range(1, n + 1):
    dp.append([])
    dp[i].append(float('inf'))
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if i == j == 1:
            dp[i].append(matrix[i-1][j-1])
        else:
            dp[i].append(min(dp[i-1][j], dp[i][j-1]) + matrix[i-1][j-1])
print(dp[n][m])
