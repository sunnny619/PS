import sys

n = int(sys.stdin.readline())

a = 0
b = []
c = {}
d = 0


for i in range(n):
    num = int(sys.stdin.readline())
    a += num
    b.append(num)
    c[num] = c.get(num, 0) +1

a = round(a/n)
# 산술평균
print(a)

b = sorted(b)
idx = n//2

# 중앙값
print(b[idx])

res = sorted(c.items(), key=lambda x: (-x[1], x[0]))

# 최빈값이 여러 개인지 확인
if len(res) > 1 and res[0][1] == res[1][1]:
    print(res[1][0])
else:
    print(res[0][0])

# 범위
print(b[-1] - b[0])