import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
graph = []
visited = [[False for _ in range(m)]for _ in range(n)]
for i in range(n):
    row = list(map(int, sys.stdin.readline().split()))
    graph.append(row)

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
count = 0


def BFS(cur_r, cur_c, graph, visited):
    q = deque()
    q.append((cur_r, cur_c))
    visited[cur_r][cur_c] = True
    area = 1

    while q:
        r, c = q.popleft()
        for i in range(4):
            nr, nc = r+dr[i], c+dc[i]
            if 0<= nr < n and 0 <= nc < m and visited[nr][nc] == False and graph[nr][nc] == 1:
                visited[nr][nc] = True
                q.append((nr, nc))
                area += 1
    return area

max_area = 0
for r in range(n):
    for c in range(m):
        if graph[r][c] == 1 and not visited[r][c]:
            count += 1
            max_area = max(max_area, BFS(r,c,graph,visited))
print(count)
print(max_area)
