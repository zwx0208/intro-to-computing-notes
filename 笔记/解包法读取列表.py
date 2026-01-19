# 写法1：常见的
a = list(map(int, input().split()))
# 写法2：星号解包
*a, = map(int, input().split())
# 写法3：更明确的列表推导
a = [int(x) for x in input().split()]


#解包法的妙用
# 读取第一个元素和剩余部分
first, *rest = map(int, input().split())
# 输入: 1 2 3 4 5
# first = 1, rest = [2, 3, 4, 5]

# 读取前两个和剩余部分
x, y, *others = map(int, input().split())
# 输入: 1 2 3 4 5
# x = 1, y = 2, others = [3, 4, 5]

# 读取除最后一个外的所有
*most, last = map(int, input().split())
# 输入: 1 2 3 4 5
# most = [1, 2, 3, 4], last = 5