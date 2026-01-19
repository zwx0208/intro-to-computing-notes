def combination_template(nums, target):
    def dfs(start, path, current_sum):
        if current_sum == target:
            result.append(path[:])    # 注意：字符串不需要[:]，因为不可变
            return
        if current_sum > target:
            return

        for i in range(start, len(nums)):    #要避免重复时，需要start参数
            # 剪枝：排序后，如果当前数已经使和超过target，后面更大，直接break
            if current_sum + nums[i] > target:
                break

            # 去重：如果当前数字和前一个相同，且不是第一次选择，跳过
            if i > start and nums[i] == nums[i - 1]:
                continue

            path.append(nums[i])
            #选择
            dfs(i, path, current_sum + nums[i])  # 递归  可重复：i
            # dfs(i+1, path, current_sum + nums[i])  # 不可重复：i+1
            path.pop()   #撤销选择，回溯


    result = []
    nums.sort()  # 重要：排序便于剪枝和去重
    dfs(0, [], 0)
    return result




#常见终止条件&剪枝

# 1. 和等于目标值
if current_sum == target:
    result.append(path[:])
    return
if current_sum > target:  # 剪枝
    return

# 2. 达到指定长度
if len(path) == k:
    result.append(path[:])
    return
if len(path) > k:  # 剪枝
    return

# 3. 到达数组末尾
if start == len(nums):
    result.append(path[:])  # 子集问题常用
    return

