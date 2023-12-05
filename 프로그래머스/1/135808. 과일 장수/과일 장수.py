def solution(k, m, score):
    sorted_scores = sorted(score)
    answer = 0
    for i in range(len(sorted_scores), m-1, -m):
        answer += sorted_scores[i-m:i][0]*m

    return answer