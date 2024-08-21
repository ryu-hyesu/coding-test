def solution(money):
    answer = 0
    
    size = len(money)
    dp = [0] * size
    
    dp[0] = 0
    dp[1] = money[1]
    
    # 첫번째 집이 선택이 안 됐을 경우
    for i in range(2, size) :
        dp[i] = max(dp[i - 1], dp[i - 2] + money[i])
    
    answer = dp[size - 1]
    
    dp[0] = money[0]
    dp[1] = money[0]
    
    # 첫번째 집이 선택이 됐을 경우
    for i in range(2, size - 1) :
        dp[i] = max(dp[i - 1], dp[i - 2] + money[i])
    
    answer = max(answer, dp[size - 2])
    
    return answer