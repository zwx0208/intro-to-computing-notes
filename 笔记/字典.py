score_groups = {3: 5, 2: 3, 1: 2}
# .keys() 只取键
print(list(score_groups.keys()))  # [3, 2, 1]
# .values() 只取值
print(list(score_groups.values()))  # [5, 3, 2]
# .items() 取键值对为元组
print(list(score_groups.items()))  # [(3, 5), (2, 3), (1, 2)]