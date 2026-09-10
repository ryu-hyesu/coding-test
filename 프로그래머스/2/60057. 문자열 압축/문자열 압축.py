def solution(s):
    answer = len(s)
    
    for x in range(1, len(s) // 2 + 1) :
        comp_len = 0
        comp = ''
        cnt = 1
        
        for i in range(0, len(s) + x, x) :
            temp = s[i:i+x]
            if comp == temp : cnt += 1
            elif comp != temp :
                comp_len += len(comp)
                if cnt > 1 : comp_len += len(str(cnt))
                comp = temp
                cnt = 1
        
        # comp_len += len(comp) + (len(str(cnt)) if cnt > 1 else 0)
        answer = min(answer, comp_len)
            
    return answer