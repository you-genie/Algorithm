def solution(players, callings):
    indices = {}
    for i, player in enumerate(players):
        indices[player] = i
    
    for calling in callings:
        idx = indices[calling]
        players[idx-1], players[idx] = players[idx], players[idx-1]
        indices[players[idx]] = idx
        indices[players[idx-1]] = idx-1
        
    return players