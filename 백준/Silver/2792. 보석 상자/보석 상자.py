n, m = map(int, input().split())
data = []

for _ in range(m) :
    data.append(int(input()))

start = 1; end = max(data)

while start <= end :
    middle = (start + end) // 2
    cnt = 0
    for jewel in data :
        cnt += (jewel // middle)
        cnt += 1 if jewel % middle != 0 else 0

    if cnt > n :
        start = middle + 1
    else :
        end = middle - 1

print(end + 1)