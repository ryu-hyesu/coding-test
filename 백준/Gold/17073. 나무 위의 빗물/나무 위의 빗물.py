from collections import defaultdict

n, w = list(map(int, input().split()))
tree = defaultdict(list)

for i in range(n - 1) :
    u, v = list(map(int, input().split()))
    tree[u].append(v)
    tree[v].append(u)
    
cnt = 0 

for root, nodes in tree.items() :
    if root != 1 and len(nodes) == 1:
        cnt += 1
        
print(round(w/cnt, 10))