def solution(k, dungeons):
    answer = []
    visited = [False]*len(dungeons)
    
    def dfs(k, count):
        for i in range(len(dungeons)):
            need, force = dungeons[i]
            if need > k:
                answer.append(count)
                continue
            
            if not visited[i]:
                visited[i] = True
                dfs(k-force, count+1)
                visited[i] = False
    dfs(k, 0)
    return max(answer)
