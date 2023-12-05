def solution(board):
    N = len(board)
    
    def valid(board, N, i, j):
        if not 0 <= i < N:
            return False
        if not 0 <= j < N:
            return False
        if board[i][j] == 1:
            return False
        return True
    
    dx_list = [-1, -1, -1, 0, 0, 1, 1, 1]
    dy_list = [-1, 0, 1, -1, 1, -1, 0, 1]
    
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                for dx, dy in zip(dx_list, dy_list):
                    if valid(board, N, i+dx, j+dy):
                        board[i+dx][j+dy] = 2
    answer = 0
       
    for i in range(N):
        for j in range(N):
            if board[i][j] == 0:
                answer += 1
    return answer