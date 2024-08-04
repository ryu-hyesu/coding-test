n, c = map(int, input().split())
data = []

for _ in range(n) :
    data.append(int(input()))

data.sort()

start = 1
end = data[-1] - data[0]
answer = 0
while start <= end :
    middle = (start + end) // 2
    cnt = 1
    for_pos = data[0]

    for pos in data :
        if (pos - for_pos) >= middle :
            cnt += 1
            for_pos = pos
    
    if cnt >= c : 
        if answer < middle : 
            answer = middle
        start = middle + 1
    else :
        end = middle - 1

print(answer)
