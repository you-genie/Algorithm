def solution(m, n, startX, startY, balls):
    answer = []
    for endX, endY in balls:
        candidates = []
        # down
        if not (startX == endX and startY > endY):
            dx, dy = startX - endX, startY + endY
            candidates.append(dx**2 + dy**2)
        # up
        if not (startX == endX and endY > startY):
            dx, dy = startX - endX, startY - (2*n - endY)
            candidates.append(dx**2 + dy**2)
        # left
        if not (startY == endY and startX > endX):
            dx, dy = startX + endX, startY - endY
            candidates.append(dx**2 + dy**2)
        # right
        if not (startY == endY and endX > startX):
            dx, dy = startX - (2*m - endX), startY - endY
            candidates.append(dx**2 + dy**2)
        
        # diag
        # if 
        answer.append(min(candidates))
    return answer