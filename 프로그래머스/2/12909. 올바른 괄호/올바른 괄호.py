from collections import deque
def solution(s):
    q=deque()
    for n in s:
        if not q:
            if n == ")":
                return False
            q.append(n)
        else:
            pop_s = q.popleft()
            if pop_s == "(":
                if n == ")":
                    continue
                else:
                    q.append(n)
                    q.append(pop_s)
    if q:
        return False
    return True