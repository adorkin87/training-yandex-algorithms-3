with open('input.txt', 'r') as f:
    source_array = f.readlines()
n = int(source_array[0])
dp = [[float('inf'), float('inf'), float('inf'), 0] for _ in range(3)]
for i in range(1, n + 1):
    dp.append(list(map(int, source_array[i].split())))
for i in range(3, n + 3):
    dp[i].append(
        min(
            (dp[i - 1][3] + dp[i][0]),
            (dp[i - 2][3] + dp[i - 1][1]),
            (dp[i - 3][3] + dp[i - 2][2])
        )
    )
print(dp[n + 2][3])
