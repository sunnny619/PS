import sys
from collections import deque

q = deque()
n = int(sys.stdin.readline())

for i in range(1, n+1):
    q.append(i)

i = 1
while len(q) > 1:
    card = q.popleft()

    if i%2==0:
        q.append(card)

    i += 1

print(q[0])