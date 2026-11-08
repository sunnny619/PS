def solution(routes):
    answer = 0
    routes = sorted(routes, key = lambda x: x[1])
    
    camera = -30001
    
    for r in routes:
        if camera < r[0]:
            camera = r[1]
            answer +=1            
        
    return answer