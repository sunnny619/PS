import sys
from collections import deque

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())
q = deque()
time = 0

board = [[0]*n for _ in range(n)]

for i in range(k):
    x, y = map(int, sys.stdin.readline().split())
    board[x-1][y-1] = 1

l = int(sys.stdin.readline())

for j in range(l):
    s, d = sys.stdin.readline().split()
    s = int(s)
    q.append((s, d))

# 우, 하, 좌, 상
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# 오른쪽 방향 기본 초기화
way = 0
x, y = 0, 0

# 뱀 길이 관리
snake = deque([(x, y)])

while True:
    time += 1

    nx, ny = x + dx[way], y + dy[way]

    if not(0 <= nx < n and 0 <= ny < n) or board[nx][ny] == 2:
        print(time)
        break

    if board[nx][ny] == 1:
        board[nx][ny] = 2
        snake.append((nx, ny))

    else:
        board[nx][ny] = 2
        snake.append((nx, ny))
        tx, ty = snake.popleft()
        board[tx][ty] = 0

    x, y = nx, ny

    if q and q[0][0] == time:
        s, d = q.popleft()
        if d == "L":
            way = (way-1)%4
        else:
            way = (way+1)%4