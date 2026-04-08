import sys

n, m = map(int, sys.stdin.readline().split())
board = []
visited = [[False for _ in range(m)]for _ in range(n)]


for _ in range(n):
    row = list(map(int, sys.stdin.readline().split()))
    board.append(row)

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

ans  = 0

def DFS(r, c, step, count, board, visited):
    global ans
    if step == 4:
        ans = max(ans, count)
        return 
    
    for i in range(4):
        nr, nc = r+dr[i], c+dc[i]
        if 0 <= nr < n and 0<= nc < m and visited[nr][nc] == False:
            visited[nr][nc] = True
            DFS(nr, nc, step +1, count + board[nr][nc], board, visited)
            visited[nr][nc] = False

def check_t(r, c):
    global ans
    for i in range(4):
        temp_sum = board[r][c]
        possible = True
        for j in range(3):
            # (i+j)%4 를 사용하면 0,1,2 / 1,2,3 / 2,3,0 / 3,0,1 방향을 순회함
            idx = (i+j)%4
            nr, nc = r+dr[idx], c+dc[idx]
            if 0 <= nr < n and 0 <= nc < m:
                temp_sum += board[nr][nc]
            else:
                possible = False
                break
        if possible:
            ans = max(ans, temp_sum)

for i in range(n):
    for j in range(m):
        visited[i][j] = True
        DFS(i, j, 1, board[i][j], board, visited)
        visited[i][j] = False
        check_t(i, j)

print(ans)