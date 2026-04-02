import sys

t = int(sys.stdin.readline())

for i in range(t):
    n = int(sys.stdin.readline())
    clothes = {}
    count = 1
    for j in range(n):
        num, c = sys.stdin.readline().split()
        clothes[c] = clothes.get(c, 0) + 1
    
    for c, num in clothes.items():
        count *= num+1
    
    print(count-1)
    