def solution(A, B):
    answer = 0
    
    A.sort()
    B.sort()
    
    pointer_A = 0
    
    for pointer_B in range(len(B)):
        if B[pointer_B] > A[pointer_A]:
            answer += 1
            pointer_A += 1
    
    
    return answer