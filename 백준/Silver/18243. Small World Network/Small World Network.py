import math
n, m = map(int, input().split())

dist = [[math.inf] * (n) for _ in range(n)]

for _ in range(m) :
    i, j = map(int, input().split())
    dist[i - 1][j - 1] = 1
    dist[j - 1][i - 1] = 1

for k in range(n) :
    for i in range(n) :
        for j in range(n) :
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

flag = True

for i in range(n) :
    for j in range(i, n) :
        if i == j : continue
        if dist[i][j] > 6 :
            flag = False
            break

if flag :
    print("Small World!")
else :
    print("Big World!")