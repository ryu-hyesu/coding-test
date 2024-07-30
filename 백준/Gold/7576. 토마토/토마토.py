from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

m, n = map(int, input().split())
tomatos = []

for _ in range(n) :
    row_tomatos = list(map(int, input().split()))
    tomatos.append(row_tomatos)

def bfs(tomatos) :
    queue = deque()

    for i in range(n) :
        for j in range(m) :
            if tomatos[i][j] == 1 : 
                queue.append((i, j))

    while queue :
        x, y = queue.popleft()

        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m :
                continue

            if tomatos[nx][ny] == 0 :
                tomatos[nx][ny] = tomatos[x][y] + 1
                queue.append((nx, ny))

bfs(tomatos)

max_days = 0
for i in range(n) :
    for j in range(m) :
        if tomatos[i][j] == 0 :
            print(-1)
            exit(0)
        else :
            max_days = max(max_days, tomatos[i][j])
print(max_days - 1)