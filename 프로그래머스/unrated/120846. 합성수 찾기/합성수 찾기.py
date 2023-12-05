def solution(n):
    sole = []
    total_set = [i for i in range(2, n+1)]
    answer = 1
    for i in range(len(total_set)):
        if total_set[i] != -1:
            answer += 1
            
            for idx, number in enumerate(total_set):
                if number != -1 and number != total_set[i] and number % total_set[i] == 0:
                    total_set[idx] = -1
    
    return n - answer