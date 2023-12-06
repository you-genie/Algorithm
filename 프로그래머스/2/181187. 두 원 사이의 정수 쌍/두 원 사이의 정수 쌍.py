import math

def solution(r1, r2):
    r1_2, r2_2 = r1**2, r2**2
    answer = 0
    
    def cal_num_positions(i, j):
        if i == j:
            return 4
        else:
            return 8
    
    # zero
    answer += (r2-r1+1)*4
    for j in range(1, math.ceil(r2/math.sqrt(2))):
        # check start
        i_s = j if j > r1 else max(math.ceil(math.sqrt(r1_2-j**2)), j)
        
        # check end
        i_e = math.floor(math.sqrt(r2_2-j**2))
        
        if i_s == j:
            answer += 4
            answer += 8*(i_e-i_s)
        else:
            answer += 8*(i_e-i_s+1)
        # for i in range(i_s, i_e+1):
        #     answer += cal_num_positions(i, j)


    return answer