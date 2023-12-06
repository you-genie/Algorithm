import numpy as np
from collections import Counter

def solution(arr):
    arr = np.array(arr)
    code_list = []
    
    def rec_compress(arr):
        arr_sum = arr.sum()
        if arr_sum == arr.shape[0]**2:
            code_list.append(1)
        elif arr_sum == 0:
            code_list.append(0)
        elif len(arr) == 1:
            code_list.append(arr[0, 0])
            return
        else:
            N = len(arr)
            sub_idx = [(0, N//2), (N//2, N)]
            sub_idx = [(sx, sy) for sx in sub_idx for sy in sub_idx]

            for sx, sy in sub_idx:
                rec_compress(arr[sx[0]:sx[1], sy[0]:sy[1]])
    
    rec_compress(arr)
    codes = dict(Counter(code_list))
    answer = [0, 0]
    if 0 in codes:
        answer[0] = codes[0]
    if 1 in codes:
        answer[1] = codes[1]
    return answer