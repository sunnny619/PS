from collections import deque
def solution(maps):
    answer = 0
    maps = [list(row) for row in maps]
    
    n = len(maps)
    m = len(maps[0])
    
    
    for i in range(n):
        for j in range(m):
            if maps[i][j] == "S":
                start = (i,j)
            if maps[i][j] == "L":
                lever = (i,j)
            if maps[i][j] == "E":
                exit = (i, j)                
        
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    
    def road(target, start):
        q = deque()
        q.append(start)
        grid = [[-1] * m for _ in range(n)]
        grid[start[0]][start[1]] = 0
        while q:
            x, y = q.popleft()
            if maps[x][y] == target:
                return grid[x][y]
            
            for i in range(4):
                new_x = x+dx[i]
                new_y = y+dy[i]
                if 0 <=new_x < n and 0<= new_y < m and maps[new_x][new_y] != "X" and grid[new_x][new_y] == -1:
                    q.append((new_x, new_y))
                    grid[new_x][new_y] = grid[x][y] +1
        return -1
    
    lever_count = road("L", start)
    if lever_count == -1:
        return -1
    exit_count = road("E", lever)
    if exit_count == -1:
        return -1
    
    return lever_count+exit_count