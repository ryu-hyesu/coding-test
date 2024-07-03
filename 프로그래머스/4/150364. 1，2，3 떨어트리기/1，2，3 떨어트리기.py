from collections import defaultdict

def solution(edges, target):
    answer = []
    node2children = create_node2children(edges)
    node2min, node2max = create_node2minmax(target)
    node2visit, visits = create_node2visit(node2children, node2min, node2max)
    if node2visit == [-1] :
        return [-1]
    node2nums = create_node2nums(node2visit, target)
    for node in visits :
        answer.append(node2nums[node].pop())
    return answer

def create_node2children(edges) :
    node2children = defaultdict(list) # 중복된 노드가 발생할 수 있으므로
    
    for parent, child in edges : 
        node2children[parent].append(child)
        
    # 자식 노드가 작은 것부터 실선으로 만들어줌
    for _, children in node2children.items():
        children.sort()
        
    return node2children
    

def create_node2minmax(target) :
    node2min = defaultdict(int)
    node2max = defaultdict(int)
    
    for node, t in enumerate(target, 1) :
        n, r = divmod(t, 3)
        if r: # 나머지가 있으면 한 번 더 방문
            n += 1
        
        node2min[node] = n
        node2max[node] = t

# if 5 min : 2 - [3, 2] , max : 5 - [1, 1, 1, 1, 1]
# if 3 min : 1 - [3] , max : 3 - [1, 1, 1]
    
    return node2min, node2max

# node -> 몇 번 방문해야 하는지
def create_node2visit(node2children, node2min, node2max) :
    node2visit = defaultdict(int)
    node2idx = defaultdict(int) # 각 노드 별로 어느 간선이 존재하는지 알고 있어야 한다
    # min과 max사이에 방문 횟수가 정해져야 한다.
    
    required = sum(node2min.values())
    visits = []
    while required : 
        p = 1
        
        while node2children[p] :
            idx = node2idx[p] # 현재 p의 자식의 인덱스
            child = node2children[p][idx] # p의 자식의 인덱스로 자식 값을 구함
            idx += 1
            if idx == len(node2children[p]):
                idx = 0
            node2idx[p] = idx
            p = child
        visits.append(p)
        node2visit[p] += 1 # 리프 노드에 도달함
        
        if node2visit[p] <= node2min[p] :
            required -= 1 
        elif node2visit[p] > node2max[p] : # 최대로 방문한 경우보다 더 돈 경우
            return [-1], visits
    return node2visit, visits
        
        
# 실제로 몇 번 방문하는지 확인 후 어떻게 방문할 것인지 만드는 함수
def create_node2nums(node2visit, target):
    node2nums = defaultdict(list)
    # 3이 최대 몇 번 나오는지에 따라서 사전순서가 결정된다.
    for node, t in enumerate(target, 1):
        nums = [] # 3이 나올 때마다 더해준다.
        three, two = divmod(t - node2visit[node], 2)
        
        for _ in range(three) :
            nums.append(3)
        
        if two :
            nums.append(2)
            
        while len(nums) < node2visit[node]:
            nums.append(1)
            
        node2nums[node] = nums #내림차순
    return node2nums