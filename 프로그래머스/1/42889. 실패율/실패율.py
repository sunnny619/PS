def solution(N, stages):
    answer = []
    
    for stage in range(1, N + 1):
        total = 0
        fail = 0
        
        for s in stages:
            if s >= stage:
                total += 1
                if s == stage:
                    fail += 1
                    
        if total == 0:
            answer.append((stage, 0))
        else:
            answer.append((stage, fail / total))
            
    answer.sort(key=lambda x: x[1], reverse=True)
    return [x[0] for x in answer]