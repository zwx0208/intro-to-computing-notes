# 要求：从users.txt中筛选出特定年龄段的人
# 输入：最小年龄和最大年龄
# 输出：该年龄段的所有人信息
# 示例：
# 输入：20, 25
ideal_people = []   # 创建空列表作为容器
i=int(input('请输入最小年龄'))
j=int(input('请输入最大年龄'))
with open('users.txt','r') as file:
    for line in file:
        line=line.strip()
        if line:
            parts=line.split(',')
            name=parts[0]
            age=int(parts[1])
            if i<= age <=j:
                ideal_people.append(f"{name},{age}")
if ideal_people:
        print(f"{i}-{j}岁的人员：", end="")
        for person in ideal_people:
            print(person, end=" ")
else:
     print("该年龄段没有人员")
