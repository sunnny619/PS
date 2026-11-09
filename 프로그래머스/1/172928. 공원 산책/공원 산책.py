def solution(park, routes):
    answer = []
    
    maps = [list(r) for r in park]
    
    n = len(maps)
    m = len(maps[0])
    
    for i in range(n):
        for j in range(m):
            if maps[i][j] == "S":
                start = (i,j)
                
    def dest(op, temp):
        x, y = temp
        if op == "N":
            new_x = x-1
            new_y = y
        if op == "S":
            new_x = x+1
            new_y = y
        if op == "E":
            new_x = x
            new_y = y+1
        if op == "W":
            new_x = x
            new_y = y-1
        
        return (new_x, new_y)
    
    for r in routes:
        x, y = start
        temp = (x, y)
        
        op, num = r.split()
        num = int(num)
        
        for i in range(num):
            new_x, new_y = dest(op, temp)
            if 0 <= new_x < n and 0 <= new_y < m and maps[new_x][new_y] != "X":
                temp = (new_x, new_y)
            else:
                temp = x, y
                break
        start = temp
    return start