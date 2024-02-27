from collections import Counter, deque

def solution(k, tangerine):
    answer = 0
    
    counter = Counter(tangerine)
    sizes = deque(sorted([(size, n) for size, n in counter.items()], key=lambda x: x[1], reverse=True))
    
    while k > 0:
        k -= sizes.popleft()[1]
        answer += 1
    return answer 