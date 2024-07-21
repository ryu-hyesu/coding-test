n = int(input())
fees = list(map(int, input().split()))
total = int(input())

start = 1
end = max(fees)

while start <= end :
    middle = (start + end) // 2
    sum = 0
    for fee in fees :
        if middle < fee :
            sum += middle 
        else :
            sum += fee

    if sum > total :
        end = middle - 1
    else :
        start = middle + 1

print(end)
