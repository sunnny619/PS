import sys

n = int(sys.stdin.readline())
board = [[0 for a in range(n)] for b in range(n)]
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

def DFS(start, cur):
    for next in range(n):
        if graph[cur][next] == 1 and board[start][next] == 0:
            board[start][next] = 1
            DFS(start, next)
for i in range(n):
    DFS(i, i)

for row in board:
    print(*row)
