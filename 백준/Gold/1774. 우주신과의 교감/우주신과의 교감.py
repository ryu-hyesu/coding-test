import sys
import math

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 입력 받기
n, m = map(int, sys.stdin.readline().split())
gods = []
for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    gods.append((x, y))

# 초기화
v = n  # 우주신의 수
parent = [i for i in range(v + 1)]

# 이미 연결된 수호신의 간선을 처리
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    union_parent(parent, a, b)

# 모든 간선 정보 구하기
edges = []
for i in range(n):
    for j in range(i + 1, n):
        cost = math.sqrt((gods[i][0] - gods[j][0]) ** 2 + (gods[i][1] - gods[j][1]) ** 2)
        edges.append((cost, i + 1, j + 1))

# 간선 비용 순으로 정렬
edges.sort()

# Kruskal 알고리즘을 이용해 최소 스패닝 트리 계산
total_cost = 0
for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        total_cost += cost

# 결과 출력
print(f"{total_cost:.2f}")
