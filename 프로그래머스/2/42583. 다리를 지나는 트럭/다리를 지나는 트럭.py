from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    q= deque([0]*bridge_length)
    
    q_weight = 0
    point = 0
    
    out = []
    
    while 1:
        if len(out) == len(truck_weights):
            break
        
        answer += 1
            
        left = q.popleft()
        q_weight -= left
        
        if left != 0:
            out.append(left)
        
        if point < len(truck_weights):
            if q_weight+truck_weights[point] <= weight:
                q.append(truck_weights[point])
                q_weight += truck_weights[point]
                point+= 1
            else:
                q.append(0)
    
    return answer