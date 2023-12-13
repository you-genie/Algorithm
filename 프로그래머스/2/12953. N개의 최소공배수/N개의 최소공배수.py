import math

def solution(arr):
    answer = 1
    for n in arr:
        gcd = math.gcd(answer, n)
        answer = answer*n//gcd
    
    return answer