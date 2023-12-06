def solution(brown, yellow):
    for x in range(1, (yellow+1)//2+1):
        if yellow % x == 0:
            y = yellow // x

            if 2*(x + y) + 4 == brown:
                return [y+2, x+2]
            
    return None