data = []
while True:
    data = input()
    if data == '0' : break
        
    length = len(data)
    middle = length % 2
    
    k = length//2
    answer = 'yes'
    
    # 짝수
    if middle == 0 :
        cnt = 0
        while k - 1 - cnt >= 0 and k + cnt < length :
            if data[k - 1 - cnt] != data[k + cnt] :
                answer = 'no'
                break
            cnt += 1
        
    else :
        cnt = 1
        while k - cnt >= 0 and k + cnt < length :
            if data[k - cnt] != data[k + cnt] :
                answer = 'no'
                break
            cnt += 1
    print(answer)
        
    
    