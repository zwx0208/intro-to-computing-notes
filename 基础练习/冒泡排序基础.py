def bubble_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        print(f"第{i + 1}轮: {arr}")

        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                print(f"  交换 {j}和{j + 1}: {arr}")

    return arr


nums = [5, 3, 8, 1]
result = bubble_sort(nums)
print("结果:", result)