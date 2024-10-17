import math
import heapq
from collections import defaultdict

def dijkstra(graph, start, end, n):
    distances = [math.inf] * (n + 1)
    distances[start] = 0
    q = []
    predecessors = [0] * (n + 1)  # 경로확인
    heapq.heappush(q, (0, start))  # q에 (cost, node)를 힙정렬로 넣는다.
    
    while q:
        current_distance, current_node = heapq.heappop(q)
        
        # 만약 연결하려고 하는 현재 노드까지의 거리가(start -> current_node) 지금 distance보다 길다면 continue
        if current_distance > distances[current_node]:
            continue
            
        for next_node, next_cost in graph[current_node]:
            distance = current_distance + next_cost  # 현재 노드로 연결됐을 때 갱신되는 노드
            
            if distance < distances[next_node]:
                distances[next_node] = distance  # 갱신
                heapq.heappush(q, (distance, next_node))
    
    return distances[end]

n, m = map(int, input().split())
graph = defaultdict(list)
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
    
print(dijkstra(graph, 1, n, n))