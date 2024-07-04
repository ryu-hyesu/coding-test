import math
import heapq
from collections import defaultdict
def dijkstra(graph, start) :
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
                
    return distances

# 입력
n, m, target = map(int, input().split())
_graph = defaultdict(list)
reverse_graph = defaultdict(list)

for _ in range(m) :
    a, b, cost = map(int, input().split())
    _graph[a].append((b,cost))
    reverse_graph[b].append((a, cost))
    
# target -> 1 ... n
result = dijkstra(_graph, target)

# 1 ... n -> target
result2 = dijkstra(reverse_graph, target)

# 결과 출력
print(max(result[i] + result2[i] for i in range(1, n + 1) if i != target))

