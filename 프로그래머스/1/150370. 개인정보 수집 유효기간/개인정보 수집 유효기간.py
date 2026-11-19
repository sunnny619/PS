def solution(today, terms, privacies):
    answer = []
    term ={}
    count = 1
    
    y, m, d = today.split(".")
    today = (int(y)*12*28)+(int(m)*28)+int(d)
    
    for t in terms:
        ty, month = t.split()
        term[ty] = month
    
    for p in privacies:
        date, ty = p.split()
        y, m, d = date.split(".")
        date = (int(y)*12*28)+(int(m)*28)+int(d)
        
        date += int(term.get(ty, 0))*28
        if date <= today:
            answer.append(count)
        count+=1
    
    return answer