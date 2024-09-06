
n = int(input())
data = list(input())

dp = [1e9] * n
dp[0] = 0

def getPrev(x) :
    if x == "O" :
        return "B"
    elif x == "J" :
        return "O"
    elif x == "B" :
        return "J"
    
for i in range(1, n) :
    for j in range(i) :
        prev = getPrev(data[i])
        
        if data[j] == prev :
            dp[i] = min(dp[i], dp[j] + (j - i) * (j - i))
            
if dp[-1] == 1e9 :
    print(-1)
else :
    print(dp[-1])
