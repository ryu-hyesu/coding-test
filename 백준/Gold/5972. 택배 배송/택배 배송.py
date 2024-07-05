from collections import defaultdict
import math
import heapq

def dijkstra(start) :
    q = []
    dist = [math.inf] * (n + 1)
    heapq.heappush(q, (0, start))
    
    while q :
        curr_cost, curr_node = heapq.heappop(q)
        
        if curr_cost > dist[curr_node] :
            continue
                
        for next_cost, next_node in graph[curr_node] :
            cost = next_cost + curr_cost
            
            if cost < dist[next_node] :
                dist[next_node] = cost
                heapq.heappush(q, (cost, next_node))
                    
    return dist[n]

n, m = map(int, input().split())
graph = defaultdict(list)
for _ in range(m) :
    a, b, cost = map(int, input().split())
    graph[a].append((cost, b))
    graph[b].append((cost, a))
        
print(dijkstra(1))