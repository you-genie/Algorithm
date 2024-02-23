from collections import defaultdict

import numpy as np

def solution(friends, gifts):
    present_matrix = [[0 for _ in friends] for _ in friends]
    
    for giver, reciever in [g_r.split() for g_r in gifts]:
        giver_idx, reciever_idx = friends.index(giver), friends.index(reciever)
        present_matrix[giver_idx][reciever_idx] += 1
        
    present_matrix = np.array(present_matrix)
    present_status = defaultdict(int)
    ratios = [sum(present_matrix[a, :]) - sum(present_matrix[:, a]) for a in range(len(friends))]

    for a, A in enumerate(friends):
        for _b, B in enumerate(friends[a+1:]):
            b = a + _b + 1
            
            if present_matrix[a][b] == present_matrix[b][a]:
                a_ratio = ratios[a]
                b_ratio = ratios[b]

                if a_ratio > b_ratio:
                    present_status[a] += 1
                elif a_ratio < b_ratio:
                    present_status[b] += 1
            elif present_matrix[a][b] > present_matrix[b][a]:
                present_status[a] += 1
            else:
                present_status[b] += 1

    answer = max(present_status.values()) if present_status else 0
    # answer = 0
    return answer