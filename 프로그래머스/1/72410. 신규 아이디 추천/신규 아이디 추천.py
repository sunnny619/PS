def solution(new_id):
    answer = ''
    new_id = new_id.lower()
    temp = ''
    for n in new_id:
        if 97 <= ord(n) <= 122 or 48 <= ord(n) <= 57 or ord(n) in (45, 46, 95):
            temp += n
            
    next = False
    for i in range(len(temp)):
        if next:
            if temp[i] != ".":
                answer += "." + temp[i]
                next = False
            else:
                continue
        elif temp[i] == ".": 
            next = True
            continue
        else:                
            answer += temp[i]
    if next:                
        answer += "."

    result = ''
    for i in range(len(answer)):
        if i == 0 or i == len(answer)-1:
            if answer[i] == ".":
                continue
        result += answer[i]
    
    if result == "":
        result += "a"
        
    answer = ''
    if len(result) >= 16:
        for i in range(15):
            answer += result[i]
        if answer[-1] == ".": 
            answer = answer[:-1]
    else:                     
        answer = result

    if len(answer) <= 2:
        while len(answer) < 3: 
            answer += answer[-1]
    return answer