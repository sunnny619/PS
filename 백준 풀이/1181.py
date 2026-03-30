import sys

n = int(sys.stdin.readline())
alphabet = set()

for i in range(n):
    alphabet.add(sys.stdin.readline().strip())

alphabet = list(alphabet)
alphabet = sorted(alphabet, key = lambda x: (len(x), x))

for j in range(len(alphabet)):
    print(alphabet[j])