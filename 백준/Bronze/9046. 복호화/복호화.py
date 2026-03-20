from collections import defaultdict

n = int(input())

for _ in range(n) :
    freq = defaultdict(int)
    
    for a in input().replace(' ', ''):
        freq[a] += 1
        
    max_v = max(freq.values())
    result = [k for k, v in freq.items() if v == max_v]
    
    if len(result) > 1:
        print("?")
    else:
        print(result[0])