import math
n, m = map(int, input().split())
dist = [[math.inf for _ in range(n + 1)] for _ in range(n + 1)]

for _ in range(m) :
    a, b = map(int, input().split())
    dist[a][b] = 1
    dist[b][a] = 1

    for i in range(1, n + 1) :
        dist[i][i] = 0

    for k in range(1, n + 1) :
      for i in range(1, n + 1) :
        for j in range(1, n + 1) :
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    result = []
    for i in range(1, n + 1) :
        sum = 0
        for j in range(1, n + 1) :
            if dist[i][j] != math.inf :
                sum += dist[i][j]
                
        result.append(sum)

print(result.index(min(result)) + 1)