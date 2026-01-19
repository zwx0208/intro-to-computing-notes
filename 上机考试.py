from collections import Counter

m, n = map(int, input().split())
students = [list(map(int, input().split())) for _ in range(m)]
scores = {}
for i in range(m * n):
    scores[i] = list(map(int, input().split()))
count_same = 0
for i in range(m):
    for j in range(n):
        current_id = students[i][j]
        current_score = scores[current_id]
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        found_same = False
        for dx, dy in directions:
            ni, nj = i + dx, j + dy
            if 0 <= ni < m and 0 <= nj < n:
                neighbor_id = students[ni][nj]
                if scores[neighbor_id] == current_score:
                    found_same = True
                    break
        if found_same:
            count_same += 1
correct_counts = [sum(scores[i]) for i in range(m*n)]
score_groups = Counter(correct_counts)
sorted_scores = sorted(score_groups.items(), key=lambda x: x[0], reverse=True)

excellent_count = 0
remaining_quota = int(m*n*0.4)
for score, count in sorted_scores:
    if count <= remaining_quota:
        excellent_count += count
        remaining_quota -= count
    else:
        break

print(count_same, excellent_count)












