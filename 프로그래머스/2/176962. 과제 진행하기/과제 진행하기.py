#입력 : 과제, 시작시간(문자열), 소요시간(문자열)
#출력 : 과제를 끝내는 순서
#시간처리 문제 -> 분으로 전환해서 계산, 배열이 무조건 시간 순서는 아님
def solution(plans):
    answer = []
    left = []
    l = len(plans)
    
    plans = sorted(plans, key = lambda x: x[1])
    
    for i in range(l):
        if i == l-1:
            answer.append(plans[i][0])
            break
            
        n, time, take = plans[i]
        
        h, m = time.split(":")
        time = (int(h)*60)+int(m)+int(plans[i][2])
        
        next_time = plans[i+1][1]
        h, m = next_time.split(":")
        next_time = (60*int(h))+int(m)
        
        if time < next_time:
            answer.append(n)
            gap = 0
            gap += next_time-time
            
            while gap:
                if left:
                    left_name, left_time = left.pop()
                    if left_time > gap:
                        left_time -= gap
                        left.append((left_name, left_time))
                        gap=0
                    else:
                        gap -= left_time
                        answer.append(left_name)
                else:
                    break
        elif time == next_time:
            answer.append(n)
        else:
            left_time = time - next_time
            left.append((n, left_time))
        
    while left:
        n, t = left.pop()
        answer.append(n)
    return answer