T = int(input())

def search(maps):
    answer = 0
    for r in maps:
        result = []
        count = 0
        linked = False
        for c in r:
            if c == 0:
                linked = False
                if count > 0:
                    result.append(count)
                count = 0
            else:
                if linked:
                    count += 1
                else:
                    count+= 1
                    linked = True
        if count > 0:
            result.append(count)
        for r in result:
            if r == k:
                answer += 1
    return answer

for test_case in range(1, T+1):
    n, k = map(int, input().split())

    c_maps = [(list(map(int, input().split()))) for _ in range(n)]
    r_maps = [list(row) for row in zip(*c_maps)]
    answer = 0

    c1 = search(c_maps)
    r1 = search(r_maps)

    print(f"#{test_case}"+" "+str(c1+r1))

