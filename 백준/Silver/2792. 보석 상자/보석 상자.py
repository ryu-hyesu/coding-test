import sys
input=sys.stdin.readline
n, m = map(int, input().split())
colors = []

for _ in range(m) :
    colors.append(int(input()))
    
start = 1
end = max(colors)
result = 0
while start <= end :
    middle = (start + end) // 2
    
    cnt = 0
    
    for color in colors :
        cnt += color // middle
        if color % middle != 0 :
            cnt += 1
    
    if cnt <= n :
        end = middle - 1
        result = middle
    else :
        start = middle + 1
        
print(result)
    