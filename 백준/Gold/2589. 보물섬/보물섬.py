from collections import deque

def bfs(land, n, m, start_x, start_y):
    queue = deque([(start_x, start_y, 0)])  # (x, y, distance)
    visited = [[False] * m for _ in range(n)]
    visited[start_x][start_y] = True
    max_distance = 0

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    while queue:
        x, y, dist = queue.popleft()
        max_distance = max(max_distance, dist)
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and land[nx][ny] == 'L':
                visited[nx][ny] = True
                queue.append((nx, ny, dist + 1))

    return max_distance

def main():
    n, m = map(int, input().split())
    land = []

    for _ in range(n):
        land.append(list(input().strip()))

    max_dist = 0

    for i in range(n):
        for j in range(m):
            if land[i][j] == 'L':
                max_dist = max(max_dist, bfs(land, n, m, i, j))

    print(max_dist)

if __name__ == "__main__":
    main()
