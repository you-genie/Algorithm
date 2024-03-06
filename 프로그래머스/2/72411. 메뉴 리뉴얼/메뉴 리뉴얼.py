from itertools import combinations
from collections import defaultdict
def solution(orders, course):
    course = sorted(course, reverse=True)
    answer = defaultdict(int)
    orders = [sorted(o) for o in orders]
    for i, a in enumerate(orders[:-1]):
        for j, b in enumerate(orders[i+1:]):
            if len(b) < len(a):
                long, short = a, b
            else:
                long, short = b, a
            
            dup = []
            for c in b:
                if c in a:
                    dup.append(c)
                    
            for n in course:
                if len(dup) >= n:
                    for comb in combinations(dup, n):
                        answer[''.join(list(comb))] += 1
    
    answer_bucket = []
    for n in course:
        a = [(k, v) for k, v in answer.items() if len(k) == n]
        if a:
            max_val = max(a, key=lambda x: x[1])[1]
            
            answer_bucket.extend([k for k, v in a if v == max_val])
    return sorted(answer_bucket)