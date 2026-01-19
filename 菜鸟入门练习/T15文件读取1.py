# 要求：先运行程序输入3个用户信息
# 然后统计：总人数、平均年龄
# 示例输入：
# 张三,25
# 李四,30
# 王五,28
# 输出：总人数：3人，平均年龄：27.7岁
total_age = 0
count = 0

with open("users.txt", "r") as file:
    for line in file:  # 逐行读取
        line = line.strip()  # 去除换行符(*)
        if line:  # 跳过空行
            parts = line.split(',')  # 按逗号分割
            name = parts[0]  # 姓名部分
            age = int(parts[1])  # 年龄部分转整数

            total_age += age
            count += 1

if count > 0:
    average_age = total_age / count
    print(f"总人数：{count}人")
    print(f"平均年龄：{average_age:.1f}岁")
else:
    print("没有数据")