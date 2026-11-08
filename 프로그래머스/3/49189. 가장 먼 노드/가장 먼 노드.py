from collections import deque
def solution(n, edge):
    answer = 0
    dist = [-1]*(n+1)
    dist[1] = 0
    q= deque()
    q.append(1)
    link = [[] for _ in range(n+1)]
    
    for x, y in edge:
        link[x].append(y)
        link[y].append(x)
    
    while q:
        n = q.popleft()
        for i in link[n]:
            if dist[i] == -1:
                q.append(i)
                dist[i] = dist[n]+1
                
    max_node = max(dist)
    for i in range(len(dist)):
        if dist[i] == max_node:
            answer +=1
    return answer