import sys

input = sys.stdin.readline

n, m = map(int, input().split())

name_to_id = {}
id_to_name = {}

for i in range(1, n + 1):
    name = input().strip() 
    name_to_id[name] = i
    id_to_name[str(i)] = name

for _ in range(m):
    query = input().strip()
    
    if query.isdigit():
        print(id_to_name[query])
    else:
        print(name_to_id[query])