def solution(picks, minerals):
    d, i, s = picks
    picks = ["diamond" for _ in range(d)] + ["iron" for _ in range(i)] + ["stone" for _ in range(s)]
    batches = [minerals[i:i+5] for i in range(0, len(minerals), 5)]
    name2score = {k: v for k, v in zip(['diamond', 'iron', 'stone'], [25, 5, 1])}
    mineral_scores = [(sum([name2score[m] for m in batch]), batch) for batch in batches]
    
    if len(picks) < len(mineral_scores):
        mineral_scores = sorted(mineral_scores[:-1], key=lambda x: x[0], reverse=True) + [mineral_scores[-1]]
    else:
        mineral_scores.sort(key=lambda x: x[0], reverse=True)
    
    answer = 0
    for pick, mineral_score in zip(picks, mineral_scores):
        _, minerals = mineral_score
        for m in minerals:
            stress = max(name2score[m] // name2score[pick], 1)
            answer += stress
    
    return answer