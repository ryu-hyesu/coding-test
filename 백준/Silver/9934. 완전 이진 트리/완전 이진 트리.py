k = int(input())
data = list(map(int, input().split()))
tree = [ [] for _ in range(k + 1) ]

def BTree(arr, x) : 
    mid = len(arr) // 2
    tree[x].append(arr[mid])

    if x == k :
        return

    BTree(arr[:mid], x + 1)
    BTree(arr[mid + 1 :], x + 1)

BTree(data, 1)

for i in range(1, k + 1) :
    print(*tree[i])