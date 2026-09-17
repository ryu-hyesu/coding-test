def solution(n):
    answer = []
    
    def hanoi(n, start, mid, to, answer) :
        if n == 1:
            return answer.append([start, to])
        hanoi(n - 1, start, to, mid, answer)
        answer.append([start, to])
        hanoi(n - 1, mid, start, to, answer)
    
    hanoi(n, 1, 2, 3, answer)
    
    return answer