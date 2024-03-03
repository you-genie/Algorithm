import math

def is_prime(n: int) -> bool:
    if n == 1: return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def convert(n: int, k: int) -> str:
    k_str = ""
    while n > 0:
        n, l = n//k, n%k
        k_str += str(l)
    
    return k_str[::-1]

def solution(n, k):
    n = convert(n, k)
    answer = 0
    for cand in n.split('0'):
        if cand and is_prime(int(cand)):
            answer += 1
    
    return answer