def solution(k, dungeons):
    answer = []
    n = len(dungeons)
    visited = [False]*n
    
    def dfs(k, count):
        answer.append(count)
        
        for i in range(n):
            if not visited[i] and k >= dungeons[i][0]:
                visited[i] = True
                dfs(k-dungeons[i][1], count+1)
                visited[i] = False

        
    dfs(k, 0)
        
        
    return max(answer)
