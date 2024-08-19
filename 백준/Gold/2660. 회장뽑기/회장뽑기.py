import sys
input = sys.stdin.readline

INF = sys.maxsize

n = int(input().rstrip())
dp = [[INF] * (n + 1) for _ in range(n + 1)]

# 간선 입력 처리
while True:
    a, b = map(int, input().split())
    if a == -1 and b == -1:
        break
    dp[a][b] = dp[b][a] = 1

# 자기 자신으로의 거리는 0으로 설정
for i in range(1, n + 1):
    dp[i][i] = 0

# 플로이드-워셜 알고리즘 적용
for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])

# 각 사람마다 가장 먼 거리 계산
A = [max(dp[i][1:]) for i in range(1, n + 1)]

# 회장의 점수와 해당 점수를 가진 사람의 수를 출력
m = min(A)
print(m, A.count(m))

# 해당 점수를 가진 사람들의 번호를 출력
for i, v in enumerate(A):
    if v == m:
        print(i + 1, end=' ')
