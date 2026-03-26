import sys
from collections import deque

a = int(sys.stdin.readline())

for i in range(a):
    q = deque([])
    list_k = []
    count = 0

    n, m = map(int, sys.stdin.readline().split())
    list_k = list(map(int, sys.stdin.readline().split(" ")))
    if n == 1:
        print(n)
        continue

    for j in range(n):
        q.append((j, list_k[j]))
    
    while q:
        max_val = max(q, key=lambda x: x[1])[1]
        
        pop_q = q.popleft()
        if pop_q[1] < max_val:
            q.append(pop_q)
            continue
        else:
            count += 1
        
        if pop_q[0] == m:
            print(count)
            break
    





