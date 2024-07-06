import math
import heapq
from collections import defaultdict
def dijkestra(start, k) :
    q = []
    heapq.heappush(q, (0, start, 0))
    dists = [[math.inf] * (k + 1) for _ in range(n + 1)]

    while q :
        curr_cost, curr_node, curr_paved = heapq.heappop(q)

        if curr_cost > dists[curr_node][curr_paved] :
            continue

        for next_node, next_cost in graph[curr_node] :
            cost = curr_cost + next_cost

            if cost < dists[next_node][curr_paved] :
                dists[next_node][curr_paved] = cost
                heapq.heappush(q, (cost, next_node, curr_paved))

            if curr_paved < k and curr_cost < dists[next_node][curr_paved + 1] :
                dists[next_node][curr_paved + 1] = curr_cost
                heapq.heappush(q, (curr_cost, next_node, curr_paved + 1))

    return min(dists[n])

n, m, k = map(int, input().split())
graph = defaultdict(list)

for _ in range(m) : 
    a, b, cost = map(int, input().split())
    graph[a].append((b, cost))
    graph[b].append((a, cost))

print(dijkestra(1, k))