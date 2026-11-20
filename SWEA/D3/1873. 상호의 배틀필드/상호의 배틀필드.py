T = int(input())

for test_case in range(1, T+1):
    h, w = map(int, input().split())
    maps = [list(input()) for _ in range(h)]

    for r in range(h):
        for c in range(w):
            if maps[r][c] == "^":
                start = (r, c, 2)
            if maps[r][c] == "v":
                start = (r, c, 3)
            if maps[r][c] == "<":
                start = (r, c, 1)
            if maps[r][c] == ">":
                start = (r, c, 0)
    q = []
    q.append(start)

    n = int(input())
    act = input()

    dx, dy = [1,-1,0,0], [0,0,-1,1]
    for a in act:
        r, c, way = q.pop()
        if a == "S":
            nr, nc = r + dy[way], c+dx[way]
            while 0 <= nr < h and 0 <= nc < w:
                if maps[nr][nc] == "*":
                    maps[nr][nc] = '.'
                    break
                if maps[nr][nc] == "#":
                    break
                nr, nc = nr + dy[way], nc + dx[way]
            q.append((r,c,way))
        else:
            if a == "U":
                z = 2
                way = 2
                maps[r][c] = "^"
            if a == "D":
                z = 3
                way = 3
                maps[r][c] = "v"
            if a == "L":
                z = 1
                way = 1
                maps[r][c] = "<"
            if a == "R":
                z = 0
                way = 0
                maps[r][c] = ">"

            nr, nc = r + dy[z], c + dx[z]
            if 0 <= nr < h and 0 <= nc < w and maps[nr][nc] == ".":
                maps[nr][nc] = maps[r][c]
                maps[r][c] = "."
                r, c = nr, nc

            q.append((r, c, way))
    print(f"#{test_case}", "".join(maps[0]))
    for r in maps[1:]:
        print("".join(r))


