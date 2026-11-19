def solution(record):
    arr = []
    name_list = {}
    answer = []
    for r in record:
        if r[0] == "E" or r[0]=="C":
            op, i, name = r.split()
            
            if op == "Enter":
                name_list[i] = name
                arr.append((i,op))
            if op == "Change":
                name_list[i] = name
            
        else:
            op, i = r.split()
            arr.append((i,op))
        
    for a in arr:
        name = name_list.get(a[0], 0)
        if a[1] == "Enter":
            answer.append(name+"님이 들어왔습니다.")
        if a[1] == "Leave":
            answer.append(name+"님이 나갔습니다.")
    return answer