def solution(picks, minerals):
    total_pick = sum(picks)
    eff_minerals = [minerals[i:i+5] for i in range(0,len(minerals),5)][:total_pick]
    eff_minerals.sort(key=lambda x:(x.count("diamond"), x.count("iron"), x.count("stone")), reverse=True)
    answer = 0
    for bundle in eff_minerals:
        for i in range(3):
            if picks[i] > 0:
                answer += fatigue(i, bundle)
                picks[i] -= 1
                break
            
    return answer

def fatigue(pick, minerals):
    if pick == 0:
        return len(minerals)
    elif pick == 1:
        result = 0
        for mineral in minerals:
            if mineral == 'diamond':
                result += 5
            else:
                result += 1
        return result
    else:
        result = 0
        for mineral in minerals:
            if mineral == 'diamond':
                result += 25
            elif mineral == 'iron':
                result += 5
            else:
                result += 1
                
        return result
