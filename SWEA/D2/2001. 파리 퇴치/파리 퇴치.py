T = int(input())

for test_case in range(1, T+1):
    n,m = map(int, input().split())

    maps = [list(map(int, list(input().split()))) for _ in range(n)]

    answer = 0
    for r in range(n-m+1):
        for c in range(n-m+1):
            total = 0
            for y in range(m):
                for x in range(m):
                    total += maps[x+c][y+r]

            answer = max(answer, total)
    print(f"#{test_case} {answer}")
