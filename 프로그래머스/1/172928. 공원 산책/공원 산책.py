def solution(park, routes):
    answer = []
    
    maps = [list(r) for r in park]
    
    n = len(maps)
    m = len(maps[0])
    
    for i in range(n):
        for j in range(m):
            if maps[i][j] == "S":
                x, y = i,j
                
    dirs = {
        "N" : (-1,0),
        "S" : (1, 0),
        "E" : (0, 1),
        "W" : (0, -1)
    }
    
    for r in routes:
        op, num = r.split()
        num = int(num)
        
        dx, dy = dirs[op]
        nx, ny = x, y
        possible = True
        for _ in range(num):
            nx += dx
            ny += dy
            
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] != "X":
                pass
            else:
                possible = False
                break
        if possible:
            x, y = nx, ny
            
    return [x, y]