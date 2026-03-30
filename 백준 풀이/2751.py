import sys

n = int(sys.stdin.readline())
result = []

for i in range(n):
    result.append(int(sys.stdin.readline().strip()))

result = sorted(result)

for j in range(len(result)):
    print(result[j])