from collections import Counter

def solution(k, tangerine):
    answer = 0
    
    counter = Counter(tangerine)
    sizes = sorted([(size, n) for size, n in counter.items()], key=lambda x: x[1], reverse=True)
    
    while k > 0:
        k -= sizes.pop(0)[1]
        answer += 1
    return answer