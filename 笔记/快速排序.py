def quicksort(array):
    # 基线条件：数组为空或只有一个元素时，直接返回
    if len(array) < 2:
        return array
    else:
        # 选择第一个元素作为基准值
        pivot = array[0]
        # 找出所有小于等于基准值的元素
        less = [i for i in array[1:] if i <= pivot]
        # 找出所有大于基准值的元素
        greater = [i for i in array[1:] if i > pivot]
        # 递归排序并合并结果
        return quicksort(less) + [pivot] + quicksort(greater)
print(quicksort([10, 5, 2, 3]))
#分治算法