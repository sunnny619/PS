import sys

while True:
    line = sys.stdin.readline().rstrip()

    if line == ".":
        break
    
    stack = []
    is_stack = True

    for s in line:
        if s == "(" or s == "[":
            stack.append(s)
        
        elif s == ")":
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                is_stack = False 
                break
        
        elif s == "]":
            if stack and stack[-1] == "[":
                stack.pop()
            else:
                is_stack = False 
                break

    if is_stack and not stack:
        print("yes")
    else:
        print("no")