n = int(input())
data =[]
for _ in range(n) :
    data.append(input())
data.sort()

cnt = 0
for i in range(n):
    flag = False
    # 현재 단어보다 길이가 긴 단어를 확인
    for j in range(i + 1, n):
        # 현재 단어가 접두사인지 확인
        if data[i] == data[j][0:len(data[i])]:
            flag = True
            break

    if not flag:
        cnt += 1

print(cnt)