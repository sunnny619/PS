def solution(rows, columns, queries):
    answer = []
    i = 1
    maps = [[0]*columns for _ in range(rows)]
    
    for r in range(rows):
        for c in range(columns):
            maps[r][c] = i
            i+=1

    for x1,y1,x2,y2 in queries:
        x1,y1,x2,y2 = x1-1, y1-1, x2-1, y2-1
        min_v = maps[x1][y1]
        temp = min_v
        
        for r in range(x1, x2):
            maps[r][y1] = maps[r+1][y1]
            min_v = min(min_v, maps[r][y1])
        for c in range(y1, y2):
            maps[x2][c] = maps[x2][c+1]
            min_v = min(min_v, maps[x2][c])
        for r in range(x2, x1, -1):
            maps[r][y2] = maps[r-1][y2]
            min_v = min(min_v, maps[r][y2])
        for c in range(y2, y1, -1):
            maps[x1][c] = maps[x1][c-1]
            min_v = min(min_v, maps[x1][c])
            
        maps[x1][y1 + 1] = temp      
        answer.append(min_v)
        
        
    return answer