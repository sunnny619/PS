T = int(input())

for test_case in range(1, T+1):
    n, m = map(int, input().split())

    maps = [list(map(int, list(input().split()))) for _ in range(n)]

    answer = 0
    #위밑오
    dx = [0, 0 ,1, -1]
    dy = [-1, 1, 0 ,0]
    #왼상 오상 오하 왼
    cx = [-1, 1, 1, -1]
    cy = [-1, -1, 1, 1]
    answer = 0
    for r in range(n):
        for c in range(n):
            total = maps[r][c]
            c_total = maps[r][c]
            for i in range(4):
                for k in range(1, m):
                    nr, nc = r+dy[i]*k, c+dx[i]*k
                    if 0<= nr < n and 0 <= nc < n:
                        total += maps[nr][nc]
                    nr, nc = r + cy[i] * k, c + cx[i] * k
                    if 0 <= nr < n and 0 <= nc < n:
                        c_total += maps[nr][nc]
            answer = max(answer, total, c_total)
    print(f"#{test_case} {answer}")

