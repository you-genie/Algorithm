import sys

def solution(sequence, k):
    N = len(sequence)
    s, e, sum_seq = N-1, N-1, sequence[N-1]
    ans_s, ans_e = sys.maxsize//2, sys.maxsize
    if sequence[0] == sequence[-1]:
        return [0, k//sequence[0]-1]
    
    
    while e >= 0:
        # print(s, e, sum_seq)
        if s < 0:
            sum_seq -= sequence[e]
            e -= 1
        elif sum_seq <= k:
            if sum_seq == k and e - s <= ans_e - ans_s and s < ans_s:
                ans_s, ans_e = s, e
            s -= 1
            sum_seq += sequence[s]
        else:
            sum_seq -= sequence[e]
            e -= 1
    
    return ans_s, ans_e
#         if N+s < 0:
#             e -= 1
#             s = e - 1
#             sum_seq = sequence[s]
#         else:
#             if sum_seq > k:            
#                 e -= 1
#                 s = e - 1
#                 sum_seq = sequence[s]
#             elif sum_seq == k:
#                 answer = [N+s, N+e-1]
#                 all_same = sequence[s] == sequence[e-1]
                
#                 if all_same:
#                     _s, _e = s-1, e-1
#                     while N+_s >= 0:
#                         if sequence[_s] != sequence[s]:
#                             break
#                         else:
#                             s, e = _s, _e
#                             _s -= 1
#                             _e -= 1
#                     answer = [N+s, N+e-1]
#                 return answer
#             else:
#                 s = s - 1
#                 sum_seq = sum_seq + sequence[s]
    
    return answer