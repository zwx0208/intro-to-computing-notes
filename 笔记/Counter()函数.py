from collections import Counter  #注意是大写

# 创建空 Counter(字典)
cnt1 = Counter()
# 从可迭代对象创建（字符串、列表等）
cnt2 = Counter("hello")  # {'h':1, 'e':1, 'l':2, 'o':1}
cnt3 = Counter([1, 2, 2, 3, 3, 3])  # {1:1, 2:2, 3:3}


cnt = Counter()
# 添加/更新元素
cnt['a'] = 1      # 直接赋值
cnt['a'] += 1     # 增加计数（如果键不存在会自动设为0）
cnt.update('abc') # 批量添加，每个字符计数+1
cnt.update({'a':2, 'b':3})  # 按字典更新
# 获取元素
cnt['a']          # 返回 'a' 的计数（不存在则返回0）
cnt.get('z', 0)   # 安全获取，不存在返回0

cnt = Counter("aabbccc")
# 1. 获取所有元素和计数
list(cnt.elements())  # ['a','a','b','b','c','c','c']
cnt.keys()            # ['a','b','c']
cnt.values()          # [2, 2, 3]
cnt.items()           # [('a',2), ('b',2), ('c',3)]
# 2. 统计功能
cnt.most_common()     # 所有元素按频率排序：[('c',3), ('a',2), ('b',2)]
cnt.most_common(2)    # 前2个：[('c',3), ('a',2)]
# 3. 总数
sum(cnt.values())     # 总元素数：7
len(cnt)              # 不同元素个数：3

a = Counter("aab")
b = Counter("abc")
# 加法（合并）
a + b  # Counter({'a':3, 'b':2, 'c':1})
# 减法（保留正数）
a - b  # Counter({'a':1})  # b从a中减去
# 交集（取最小值）
a & b  # Counter({'a':1, 'b':1})
# 并集（取最大值）
a | b  # Counter({'a':2, 'b':1, 'c':1})

# 1. 统计出现次数最多的元素
text = "hello world"
most_common = Counter(text).most_common(1)  # [('l', 3)]
# 2. 找出出现次数 > n 的元素
cnt = Counter([1,1,2,2,2,3])
{n for n, count in cnt.items() if count > 1}  # {1, 2}
# 3. 两个列表元素差异
list1 = ['a','a','b','c']
list2 = ['a','b','b']
diff = Counter(list1) - Counter(list2)  # {'a':1, 'c':1}
# 4. 频率标准化
cnt = Counter("aabbc")
total = sum(cnt.values())
normalized = {k: v/total for k, v in cnt.items()}
# {'a':0.4, 'b':0.4, 'c':0.2}

