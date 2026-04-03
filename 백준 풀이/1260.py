import sys
from collections import deque

n, m, v = map(int, sys.stdin.readline().split())

adj = [[] for i in range(n+1)]
dfs_visited = [False] *(n+1)
bfs_visited = [False] *(n+1)

dfs_answer = []
bfs_answer = []

for i in range(m):
    v1, v2 = map(int, sys.stdin.readline().split())
    adj[v1].append(v2)
    adj[v2].append(v1)

for j in range(len(adj)):
    adj[j].sort()

#dfs
def DFS(start, adj):
    dfs_visited[start] = True

    for i in range(len(adj[start])):
        cur = adj[start][i]
        if not dfs_visited[cur]:
            dfs_answer.append(cur)
            DFS(cur, adj)

#bfs
q= deque()
def BFS(v, adj):
    q.append(v)

    while q:
        cur = q.popleft()
        if not bfs_visited[cur]:
            bfs_visited[cur] = True
            bfs_answer.append(cur)

            for c in adj[cur]:
                if not bfs_visited[c]:
                    q.append(c)

dfs_answer.append(v)
DFS(v, adj)
BFS(v, adj)
print(*dfs_answer)
print(*bfs_answer)


