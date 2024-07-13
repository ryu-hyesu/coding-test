# DP 테이블 초기화 (모두 0으로 초기화)
dp = [[[0 for _ in range(105)] for _ in range(105)] for _ in range(105)]

# DP 테이블 채우기
for a in range(105):
    for b in range(105):
        for c in range(105):
            if a <= 50 or b <= 50 or c <= 50:
                dp[a][b][c] = 1
            elif a > 70 or b > 70 or c > 70:
                dp[a][b][c] = dp[70][70][70]
            elif a < b < c:
                dp[a][b][c] = dp[a][b][c - 1] + dp[a][b - 1][c - 1] - dp[a][b - 1][c]
            else:
                dp[a][b][c] = dp[a - 1][b][c] + dp[a - 1][b - 1][c] + dp[a - 1][b][c - 1] - dp[a - 1][b - 1][c - 1]

while True:
    # 입력 받기
    user_input = input()

    # 입력을 공백을 기준으로 분리하고 정수로 변환
    a, b, c = map(int, user_input.split())

    if a == -1 and b == -1 and c == -1:
        break

    # 입력된 값을 DP 인덱스에 맞게 변환하여 출력
    if a <= 0 or b <= 0 or c <= 0:
        print(f"w({a}, {b}, {c}) = 1")
    elif a > 20 or b > 20 or c > 20:
        print(f"w({a}, {b}, {c}) = {dp[70][70][70]}")
    else:
        print(f"w({a}, {b}, {c}) = {dp[a + 50][b + 50][c + 50]}")
