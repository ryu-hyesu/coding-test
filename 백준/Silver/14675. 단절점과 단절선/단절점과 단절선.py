import sys

n = int(input())
trees = [[] for _ in range(n + 1)]
for _ in range(n - 1) :
    a, b = map(int,sys.stdin.readline().split())
    trees[a].append(b)
    trees[b].append(a)
    
q = int(input())
for _ in range(q) :
    t, k = map(int,sys.stdin.readline().split())
    
    if t == 1 :
        if (len(trees[k]) < 2) :
            print("no")
        else :
            print("yes")
    else :
        print("yes")
    