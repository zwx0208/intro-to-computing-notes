def analyze_scores(scores):
    count = 0
    total=0
    for score in scores:
        if score >= 60:
            count += 1
        total+=score
    return count,total
scores_list= [85, 92, 45, 78, 63, 95, 51]
print(analyze_scores(scores_list))