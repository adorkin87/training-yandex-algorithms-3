with open('input.txt', 'r') as f:
    str = f.readline()
n, k = map(int, str.split(' '))
if n == 1:
    dp = [0] * (n + k - 1)
else:
    dp = [0] * (n + k - 2)
dp[k - 2] = dp[k - 1] = 1
for i in range(k, n + k - 2):
    sum = 0
    index = i
    for _ in range(k):
        sum += dp[index - 1]
        index -= 1
    dp[i] = sum
result = dp[-1]
print(result)
