import sys
from itertools import product

t = int(sys.stdin.readline())

for i in range(t):
    n = int(sys.stdin.readline())
    dp = [0]*(n+1)

    if n == 0:
        print(0)
        continue
    if n == 1:
        print(1)
        continue
    if n == 2:
        print(2)
        continue
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4
    
    for j in range(4, n+1):
        dp[j] = dp[j-1] + dp[j-2] + dp[j-3]

    print(dp[n])