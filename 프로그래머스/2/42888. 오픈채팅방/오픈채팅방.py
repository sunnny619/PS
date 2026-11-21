def solution(record):
    names = {}
    arr = []
    answer = []
    for r in record:
        if r[0] == "L":
            op, user_id = r.split()
            arr.append((op, user_id))
        else:
            op, user_id, name = r.split()
            names[user_id] = name
            if op == "Enter":
                arr.append((op, user_id))
    
    for op, user_id in arr:
        name = names.get(user_id, 0)
        if op == "Enter":
            answer.append(name+"님이 들어왔습니다.")
        if op == "Leave":
            answer.append(name+"님이 나갔습니다.")

    return answer