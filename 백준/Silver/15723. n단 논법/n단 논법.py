from collections import deque
from collections import defaultdict

def bfs(start, end) :
    q = deque([start])
    visited = defaultdict(bool)

    while q :
        curr_node = q.popleft()

        if curr_node == end : 
            return True

        for next_node in graph[curr_node] :
            if not visited[next_node] :
                q.append(next_node)
                visited[next_node] = True

    return False

n = int(input())
graph = defaultdict(list)

for _ in range(n) :
    a, _, b = input().split()
    graph[a].append(b)

m = int(input())

for _ in range(m) :
    a, _, b = input().split()
    if bfs(a, b) :
        print("T")
    else :
        print("F")