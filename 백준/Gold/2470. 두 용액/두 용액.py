n = int(input())

data = list(map(int, input().split()))
data.sort()

left = 0
right = len(data) - 1
result = [data[left], data[right]]
answer = abs(data[left] + data[right])

while left < right :
    left_result = data[left]
    right_result = data[right]
    
    sum_result = left_result + right_result
    
    if abs(sum_result) < answer :
        answer = abs(sum_result)
        result = [left_result, right_result]
        if answer == 0 :
            break
    if sum_result < 0 :
        left += 1
    else :
        right -= 1
        
print(*result)
        