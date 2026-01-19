import bisect
bisect.bisect_left(arr, x)   # 第一个 ≥ x 的位置索引
bisect.bisect_right(arr, x)  # 第一个 > x 的位置索引  bisect.bisect() 是 bisect_right 的别名。

#(1) 求 ≤ x 的元素个数
count = bisect.bisect_right(arr, x)  # 直接就是数量
#(2) 求 < x 的元素个数
count = bisect.bisect_left(arr, x)
#(3) 求 ≥ x 的元素个数
count = len(arr) - bisect.bisect_left(arr, x)
#(4) 在有序列表插入元素，保持有序
bisect.insort_left(arr, x)   # 插入在第一个 ≥ x 的位置前
bisect.insort_right(arr, x)  # 插入在第一个 > x 的位置前