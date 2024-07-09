
  
# 나머지 구할 변수  
mod = 1000000000  
  
N = int(input())  
# 0~9까지 10개의 수이므로  
# 1<<10 == 2^10 == 1024  
# 1024가 의미하는 것은 계단의 숫자를 사용했는지 안했는지에 대한 경우의수  
# 저장되는 건 그 전의 자릿수가 +1이나 -1로 끝난 것의 합을 모두 더해주는 것이다.  
dp = [[0 for _ in range(1<<10)] for _ in range(10)]  
  
# 시작자리 1로 설정해준다.  
for i in range(1, 10):  
    dp[i][1<<i] = 1  
  
# 자릿수 만큼 순회  
for i in range(1, N):  
    # 각 자릿수에서의 정보를 담을 배열  
    dp_next = [[0 for _ in range(1024)] for _ in range(10)]  
    # 0~ 9까지 순회  
    for j in range(10):  
        # 모든 비트에 대해 순회 (비트마스킹)  
        # 위의 설명처럼 1024는 계단 숫자 사용 여부에 대한 경우의 수        # 3의 경우 2 또는 4를 사용하는 경우가 있다.        
        for k in range(1024):  
            # 0과 9의 경우 앞뒤로 한칸씩 밖에 못 더해주므로 조건문을 이용하여 걸러준다.  
            if j < 9:  
                dp_next[j][k | (1 << j)] = (dp_next[j][k | (1 << j)] + dp[j+1][k]) % mod  
            if j > 0:  
                dp_next[j][k | (1 << j)] = (dp_next[j][k | (1 << j)] + dp[j - 1][k]) % mod  
  
    dp = dp_next  
  
print(sum(dp[i][1023] for i in range(10)) % mod)