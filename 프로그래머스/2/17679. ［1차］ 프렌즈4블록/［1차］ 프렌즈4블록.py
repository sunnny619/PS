def solution(m, n, board):
    answer = 0
    board = [list(b) for b in board]  
    
    while True:
        block = set()
        
        for i in range(m - 1):
            for j in range(n - 1):
                if board[i][j] != 0:
                    if board[i][j] == board[i][j+1] == board[i+1][j] == board[i+1][j+1]:
                        block.add((i, j))
                        block.add((i, j+1))
                        block.add((i+1, j))
                        block.add((i+1, j+1))
                        
        if block:
            for x, y in block:
                board[x][y] = 0
                answer += 1
        else:
            break
        
        for j in range(n):
            survived = [board[i][j] for i in range(m) if board[i][j] != 0]
            empty_count = m - len(survived)
            new_column = [0] * empty_count + survived
            for i in range(m):
                board[i][j] = new_column[i]
                
    return answer