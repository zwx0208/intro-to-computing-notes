'''递归三要素检查：
1.基准情况：n == 0 or n == 1（停止条件）
2.递归调用：factorial(n-1)（调用自身）
3.问题规模减小：n → n-1（问题变小）
递归思维：不要纠结递归的详细过程，相信函数已经能解决小问题！'''
# T1
# 要求：用递归方法找出列表中的最大值
# 不能使用max()函数或循环
# 示例：
# 输入：[3, 1, 4, 1, 5, 9, 2]
# 输出：9
def find_max(lst):
    if len(lst) == 0:
        return None
    if len(lst) == 1:
        return lst[0]
    first = lst[0]
    rest_max = find_max(lst[1:])  # ⭐递归（要在函数内调用自身）
    return first if first > rest_max else rest_max

print(find_max([3, 1, 4, 1, 5, 9, 2]))


'''def 套娃(问题):
    if 问题足够小:          # 最小娃娃
        return 直接解决
    
    小问题 = 把问题拆小       # 拆开外层娃娃
    小问题的答案 = 套娃(小问题)  # ⭐ 套娃！打开内层娃娃
    
    return 组合(小问题的答案)   # 把娃娃装回去'''