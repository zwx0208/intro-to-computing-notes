def binary_search_basic(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2  # 取中间位置
        print(f"left={left}, right={right}, mid={mid}, arr[mid]={arr[mid]}")

        if arr[mid] == target:
            return mid  # 找到目标，返回索引
        elif arr[mid] < target:
            left = mid + 1  # 目标在右半部分
        else:
            right = mid - 1  # 目标在左半部分

    return 'none'  # 没找到


arr = [1, 3, 5, 7, 9, 11, 13, 15]
print(binary_search_basic(arr, 9))