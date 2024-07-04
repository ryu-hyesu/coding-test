import math
import heapq
from collections import defaultdict
def dijkstra(start, target) :
    q = []
    heapq.heappush(q, (0, start))
    distances = [math.inf] * (n + 1)

    while q :
        current_distance, current_node = heapq.heappop(q)

        if current_distance > distances[current_node] : # 다른 거리, 같은 노드 거름 + 이미 갱신한 거 거름
            continue

        for next_node, next_distance in graph[current_node] :
            distance = next_distance + current_distance

            if distance < distances[next_node] : # 갱신
                distances[next_node] = distance
                heapq.heappush(q, (distance, next_node))

    # 1 .. n -> target
    if start != target :
        return distances[target]
    # target -> 1 ... n
    return distances

# 입력
n, m, target = map(int, input().split())
graph = defaultdict(list)

for _ in range(m) :
    a, b, cost = map(int, input().split())
    graph[a].append((b,cost))

result = defaultdict(int)

# target -> 1 ... n
result = dijkstra(target, target)

# 1 ... n -> target
for i in range(1, n + 1) :
    if i != target :
        result[i] += dijkstra(i, target)

result[0] = 0
result[target] = 0

# 결과 출력
print(max(result))

