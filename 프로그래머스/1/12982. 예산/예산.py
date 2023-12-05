def solution(d, budget):
    sorted_d = sorted(d)
    answer = 0
    b = budget
    for data in sorted_d:
        if b - data >= 0:
            answer += 1
            b -= data
        else:
            break
    
    return answer