import sys

n, m = map(int, sys.stdin.readline().split())
r, c, d = map(int, sys.stdin.readline().split())
room = []
count = 0

for i in range(n):
    room.append(list(map(int, sys.stdin.readline().split())))

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def solve():
    global r, c, d, count
    while True:
        if room[r][c] == 0:
            room[r][c] = 2
            count += 1
    
        found_dirty = False

        # 청소할 곳 찾기
        for _ in range(4):
            d = (d+3) % 4
            nr, nc = r + dr[d], c + dc[d]

            if 0 <= nr < n and 0 <= nc < m and room[nr][nc] == 0:
                r, c = nr, nc
                found_dirty = True
                break
    
        if not found_dirty:
            back_r, back_c = r - dr[d], c - dc[d]

            if 0<= back_r < n and 0 <= back_c < m and room[back_r][back_c] != 1:
                r, c = back_r, back_c
            else:
                return(count)

print(solve())
