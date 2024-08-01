from collections import deque
n, m = map(int, input().split())

data = []
for _ in range(n) :
    row = list(map(int, input().split()))
    data.append(row)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(a, b) :
    visited = [[False for _ in range(m)] for _ in range(n)]
    counted = [[0 for _ in range(m)] for _ in range(n)]
    queue = deque()
    queue.append((a, b))
    visited[a][b] = True

    while queue :
        x, y = queue.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] :
                if data[nx][ny] == 0 : 
                    visited[nx][ny] = True
                    continue

                visited[nx][ny] = True
                counted[nx][ny] = counted[x][y] + 1
                queue.append((nx, ny))

    return counted, visited

counted = []
visited = []
flag = False
for i in range(n) :
    for j in range(m) :
        if data[i][j] == 2 :
            counted, visited = dfs(i, j)
            flag = True
            break
    if flag : break

for i in range(n) :
    for j in range(m) :
        if not visited[i][j] :
            if data[i][j] == 0 : counted[i][j] = 0
            else : counted[i][j] = -1

for i in range(n) :
    print(*counted[i])



