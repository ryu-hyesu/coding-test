import sys
sys.setrecursionlimit(10**6)
n = int(sys.stdin.readline())
nodes = [[] for i in range(n + 1)]

for i in range(n - 1) :
    a, b = map(int, sys.stdin.readline().split())
    nodes[a].append(b)
    nodes[b].append(a)

visited = [False for i in range(n + 1)]
parent = [0 for i in range(n + 1)]

def dfs(node) :
    visited[node] = True
    for i in nodes[node] :
        if not visited[i] :
            parent[i] = node
            dfs(i)
                
dfs(1)

for i in range(2, n + 1):
    print(parent[i])