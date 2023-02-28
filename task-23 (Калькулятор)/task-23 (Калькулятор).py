n = int(input())
dp = [[_ for _ in range(2)], [_ for _ in range(2)]]
if n == 1:
    print('0\n1')
elif n == 2:
    print('1\n2')
else:
    for i in range(3, n + 1):
        if i % 3 == 0 or i % 2 == 0:
            min_number = []
            min_number.append(dp[0][(i // 3) - 1] if i % 3 == 0 else float('inf'))
            min_number.append(dp[0][(i // 2) - 1] if i % 2 == 0 else float('inf'))
            min_number.append(dp[0][i - 2])
            min_val, min_id = min((val, id) for id, val in enumerate(min_number))
            dp[0].append(min_val + 1)
            if min_id == 0:
                dp[1].append(i // 3)
            elif min_id == 1:
                dp[1].append(i // 2)
            else:
                dp[1].append(i-1)
        else:
            dp[0].append(dp[0][i - 2] + 1)
            dp[1].append(i-1)
    result = [n, dp[1][n-1]]
    pointer = dp[1][-1]
    for _ in range(dp[0][n - 1] - 1):
        result.append(dp[1][pointer - 1])
        pointer = dp[1][pointer - 1]
    print(dp[0][n - 1])
    print(*result[::-1])
