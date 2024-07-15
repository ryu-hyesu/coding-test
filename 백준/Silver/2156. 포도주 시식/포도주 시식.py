import math
import sys
input = sys.stdin.read

data = input().split()
n = int(data[0])
data = list(map(int, data[1:n+1]))

dp = [0] * n

if n == 1:
    print(data[0])
    sys.exit()

dp[0] = data[0]
dp[1] = data[0] + data[1]

if n > 2:
    dp[2] = max(data[2] + data[0], data[2] + data[1], dp[1])

# 현재 마시지 않는 경우 dp[i - 1]
# 현재 마시는 경우
# (1) 이전 잔은 마시지 않는 경우 dp[i - 2] + data[i]
# (2) 이전 잔도 마시는 경우 dp[i - 3] + data[i - 1] + data[i]
for i in range(3, n):
    dp[i] = max(dp[i-1], dp[i-2] + data[i], dp[i-3] + data[i-1] + data[i])

print(dp[n-1])
