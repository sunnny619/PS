from collections import deque
def solution(maps):
    n = len(maps)
    m = len(maps[0])
    dx = [-1, 1, 0 ,0]
    dy = [0, 0 ,-1, 1]
    
    level_count = 0
    exit_cout = 0
    
    level_start = (0,0)

    for i in range(n):
            for j in range(m):
                if maps[i][j] == "S":
                    start = (i,j)
    
    def bfs(start, target):
        nonlocal level_start
        q = deque()
        x, y = start
        q.append((x, y))
        board = [[-1]*m for _ in range(n)]
        board[x][y] = 0
        while q:
            x, y = q.popleft()
            for i in range(4):
                nx = dx[i]+x
                ny = dy[i]+y

                if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] != "X" and board[nx][ny] == -1:
                    board[nx][ny] = board[x][y] +1
                    if maps[nx][ny] == target:
                        lever_count = board[nx][ny]
                        level_start = (nx, ny)
                        return lever_count
                    q.append((nx,ny))
        return -1
    
    lever_count = bfs(start, "L")
    if lever_count == -1:
        return -1
    exit_count = bfs(level_start, "E")
    if exit_count == -1:
        return -1
                    
    return lever_count+exit_count