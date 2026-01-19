def nextGreaterElement(nums):
    n = len(nums)
    res = [-1] * n
    stack = []  # 存下标，其对应列表中的值是递减的
    for i in range(n):
        # 当前元素大于栈顶元素时，栈顶元素找到了右边更大的第一个数，栈顶元素的前一个元素是它左边比它大的第一个数
        while stack and nums[i] > nums[stack[-1]]:
            idx = stack.pop()
            res[idx] = nums[i]
        stack.append(i)
    return res

print(nextGreaterElement([2, 1, 5, 6, 2, 3]))
# 输出: [5, 5, 6, -1, 3, -1]   每个数对应的值是它右边第一个比它大的数,-1表示没有