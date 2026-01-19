n,w=map(int,input().split())
items = []
for _ in range(n):
    v, weight = map(int, input().split())
    items.append((v / weight, v, weight))
items.sort(reverse=True)
total_value = 0
remaining_weight = w
for unit_value, value, weight in items:
    if remaining_weight >= weight:
        total_value += value
        remaining_weight -= weight
    else:
        total_value += unit_value * remaining_weight
        break
print(f"{total_value:.1f}")