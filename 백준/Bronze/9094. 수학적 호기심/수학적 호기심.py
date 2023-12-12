def count_integer_pairs(n, m):
    """
    Counts the number of integer pairs (a, b) such that 0 < a < b < n and 
    (a^2 + b^2 + m) / (a * b) is an integer.
    
    :param n: Upper bound for a and b
    :param m: Given integer m
    :return: Count of integer pairs satisfying the condition
    """
    count = 0
    for a in range(1, n):
        for b in range(a + 1, n):
            if (a**2 + b**2 + m) % (a * b) == 0:
                count += 1
    return count

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    T = int(input())
    for _ in range(T):
        n, m = map(int, input().split())
        print(count_integer_pairs(n, m))
