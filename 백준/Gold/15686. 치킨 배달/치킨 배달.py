from itertools import combinations
from collections import deque
import math
n, m = map(int, input().split())

data = []
chickens = []
house = []

for _ in range(n) :
    temp = list(map(int, input().split()))
    data.append(temp)

for i in range(n) :
    for j in range(n) :
        if data[i][j] == 2 :
            chickens.append((i, j))
            data[i][j] = 0
        if data[i][j] == 1 :
            house.append((i, j))

result = math.inf

for chicken in combinations(chickens, m) :
    chicken_dist = 0
    for h in house :
        h_dist = math.inf # 집 - 치킨
        for c in chicken :
            dist = abs(h[0] - c[0]) + abs(h[1] - c[1]) 
            h_dist = min(h_dist, dist)

        chicken_dist += h_dist
    
    result = min(result, chicken_dist)

print(result)
