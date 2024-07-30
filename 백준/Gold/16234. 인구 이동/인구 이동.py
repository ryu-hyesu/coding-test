from collections import deque
n, L, R = map(int, input().split())
data = []

for _ in range(n) :
    data_list = list(map(int, input().split()))
    data.append(data_list)

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def bfs(visited, a, b) :
    visited_nodes = set()
    queue = deque()

    sum_diff = data[a][b]
    cnt = 1
    queue.append((a, b))
    visited_nodes.add((a, b))
    visited[a][b] = True

    while queue :
        x, y = queue.popleft()

        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] :
                diff = abs(data[nx][ny] - data[x][y])
                if L <= diff <= R :
                    visited[nx][ny] = True
                    visited_nodes.add((nx, ny))
                    sum_diff += data[nx][ny]
                    cnt += 1
                    queue.append((nx, ny))

    result = sum_diff // cnt

    if cnt == 1 : 
        return False

    for i in range(n) :
       for j in range(n) :
           if (i, j) in visited_nodes :
                data[i][j] = result
    return True

flag = True
cnt = 0
while flag :
    flag = False
    cnt += 1

    visited = [[False for _ in range(n)] for _ in range(n)]

    for i in range(n) :
        for j in range(n) :
            if not visited[i][j] and bfs(visited, i, j) :
                flag = True


print(cnt - 1)