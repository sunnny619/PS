'''
한자리 숫자가 적힌 종이 조각이 흩어져있습니다. 흩어진 종이 조각을 붙여 소수를 몇 개 만들 수 있는지 알아내려 합니다.

각 종이 조각에 적힌 숫자가 적힌 문자열 numbers가 주어졌을 때, 종이 조각으로 만들 수 있는 소수가 몇 개인지 return 하도록 solution 함수를 완성해주세요.

제한사항
numbers는 길이 1 이상 7 이하인 문자열입니다.
numbers는 0~9까지 숫자만으로 이루어져 있습니다.
"013"은 0, 1, 3 숫자가 적힌 종이 조각이 흩어져있다는 의미입니다.
입출력 예
numbers	return
"17"	3
"011"	2
'''
# 조합 뽑아내기 : permutations

from itertools import permutations

def solution(numbers):
    answer = 0
    all_numbers = set()
    
    card = list(numbers)
    
    for i in range(1, len(numbers)+1):
        for p in permutations(card, i):
            num = int("".join(p))
            all_numbers.add(num)
    
    for n in all_numbers:
        if n < 2:
            continue
            
        is_prime = True
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                is_prime = False
                break  
                
        if is_prime:
            answer += 1
        
    return answer