import math
import sys
input = sys.stdin.read
data = input().split()
n = int(data[0])
wine = list(map(int, data[1:n+1]))

# DP array to store the maximum wine amount
dp = [0] * n

if n == 1:
    print(wine[0])
    sys.exit()

dp[0] = wine[0]
dp[1] = wine[0] + wine[1]

if n > 2:
    dp[2] = max(wine[2] + wine[0], wine[2] + wine[1], dp[1])

for i in range(3, n):
    dp[i] = max(dp[i-1], dp[i-2] + wine[i], dp[i-3] + wine[i-1] + wine[i])

print(dp[n-1])
