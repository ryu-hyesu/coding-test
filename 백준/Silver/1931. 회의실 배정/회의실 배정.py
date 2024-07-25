n = int(input())

data = []

for _ in range(n) :
    data.append(list(map(int, input().split())))
    
data.sort(key=lambda x:(x[1], x[0]))
last = 0
cnt = 0
for start, end in data :
    if start >= last :
        cnt += 1
        last = end
        
print(cnt)