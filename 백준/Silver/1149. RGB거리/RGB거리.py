n = int(input())
dp = []

# R : 0, G : 1, B : 2
for _ in range(n) :
    rgb = list(map(int, input().split()))
    dp.append(rgb)

for i in range(1, n) :
    # red
    dp[i][0] += min(dp[i - 1][1], dp[i - 1][2])

    # blue
    dp[i][1] += min(dp[i - 1][0], dp[i - 1][2])

    # green
    dp[i][2] += min(dp[i - 1][0], dp[i - 1][1])

print(min(dp[n - 1]))