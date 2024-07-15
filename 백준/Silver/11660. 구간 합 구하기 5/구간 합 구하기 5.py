import sys
input = sys.stdin.read

data = input().split()
index = 0

n = int(data[index])
index += 1
m = int(data[index])
index += 1

array = []
for _ in range(n):
    row = list(map(int, data[index:index+n]))
    array.append(row)
    index += n

dp = [[0] * (n + 1) for _ in range(n + 1)]

# DP 배열 채우기
for i in range(1, n + 1):
    for j in range(1, n + 1):
        dp[i][j] = array[i - 1][j - 1] + dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1]

results = []
for _ in range(m):
    x1 = int(data[index])
    index += 1
    y1 = int(data[index])
    index += 1
    x2 = int(data[index])
    index += 1
    y2 = int(data[index])
    index += 1
    
    result = dp[x2][y2] - dp[x1 - 1][y2] - dp[x2][y1 - 1] + dp[x1 - 1][y1 - 1]
    results.append(result)

sys.stdout.write("\n".join(map(str, results)) + "\n")
