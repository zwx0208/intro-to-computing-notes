# 要求：用递归判断数组是否从小到大有序
# 示例：
# 输入：[1, 2, 3, 4, 5] → 输出：True
# 输入：[1, 3, 2, 4] → 输出：False
# 输入：[7] → 输出：True

def is_sorted(lst):
    if len(lst)<=1:
        return True
    elif lst[0]<=lst[1]&is_sorted(lst[1:]):
        return True
    else:
        return False

print(is_sorted([1, 2, 3, 4, 5]))
print(is_sorted([1, 3, 2, 4]))
print(is_sorted([7]))