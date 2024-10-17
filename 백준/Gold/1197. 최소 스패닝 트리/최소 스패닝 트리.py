import sys
import heapq
input = sys.stdin.readline

def prim(start, n, graph):
    visited = [False] * (n + 1)
    heap = [(0, start)]  # (가중치, 노드)
    total_weight = 0
    
    while heap:
        weight, node = heapq.heappop(heap)
        
        if visited[node]:
            continue
            
        visited[node] = True
        total_weight += weight
        
        for next_weight, next_node in graph[node]:
            if not visited[next_node]:
                heapq.heappush(heap, (next_weight, next_node))
                
    return total_weight

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    # 양방향 간선
    graph[a].append((c, b))
    graph[b].append((c, a))

print(prim(1, n, graph))