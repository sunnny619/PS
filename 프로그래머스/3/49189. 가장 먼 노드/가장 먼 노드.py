from collections import deque
def solution(n, edge):
    answer = 0
    link = [[] for _ in range(n+1)]
    q= deque()
    dist = [-1] *(n+1)
    dist[1] = 0
    
    for x,y in edge:
        link[x].append(y)
        link[y].append(x)
        
    q.append(1)

    while q:
        node = q.popleft()
        for next_node in link[node]:
            if dist[next_node] == -1:
                dist[next_node] = dist[node]+1
                q.append(next_node)
    max_dist = max(dist)
    
    for i in range(len(dist)):
        if dist[i] == max_dist:
            answer+=1
    return answer