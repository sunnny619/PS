import sys

n = int(sys.stdin.readline())
idx = 0
num_list = []
sign_list = []

is_stack = True

for i in range(n):
    num = int(sys.stdin.readline())

    while idx < num:
        idx += 1
        num_list.append(idx)
        sign_list.append("+")
    
    if num_list[-1] == num:
        num_list.pop()
        sign_list.append("-")
    
    elif num_list[-1] > num:
        is_stack = False
        break

if is_stack:
    for sign in sign_list:
        print(sign)
else:
    print("NO")
