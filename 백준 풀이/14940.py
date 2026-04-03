import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
r = 0
c = 0
board = []
visited = [[-1 for _ in range(m)] for _ in range(n)]

# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for i in range(n):
    row = list(map(int, sys.stdin.readline().split()))
    for j in range(len(row)):
        if row[j] == 2:
            r, c = i, j
        if row[j] == 0:
            visited[i][j] = 0
    board.append(row)

visited[r][c] = 0

q = deque()
def BFS(s_r, s_c, board):
    q.append((s_r, s_c))

    while q:
        r, c = q.popleft()
        for i in range(4):
            nr, nc = r+dr[i], c+dc[i]
            if 0 <= nr < n and 0 <= nc < m:
                if board[nr][nc] == 1 and visited[nr][nc] == -1:
                    visited[nr][nc] = visited[r][c] + 1
                    q.append((nr,nc))

BFS(r, c, board)

for row in visited:
    print(*row)