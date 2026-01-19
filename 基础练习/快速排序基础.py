def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]  # 选择中间元素作为基准
    print(f"基准元素: {pivot}")

    left = [x for x in arr if x < pivot]  # 小于基准
    middle = [x for x in arr if x == pivot]  # 等于基准
    right = [x for x in arr if x > pivot]  # 大于基准

    print(f"分区: {left} + {middle} + {right}")

    # 递归排序左右部分，合并结果(递归运用*)
    return quick_sort(left) + middle + quick_sort(right)


# 测试
nums = [5, 3, 8, 1, 2,4,2,3,5]
result = quick_sort(nums)
print("快速排序结果:", result)


