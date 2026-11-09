import heapq
def solution(n, k, enemy):
    heap = []
    
    for i, e in enumerate(enemy):
        n = n - e
        heapq.heappush(heap, -e)
        
        if n < 0:
            if k > 0:
                n += -heapq.heappop(heap)
                k -=1

            else:
                return i
    
    return len(enemy)