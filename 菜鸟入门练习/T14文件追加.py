# 要求：创建程序，循环输入用户信息（姓名,年龄）
# 将信息保存到文件 users.txt 中
# 输入"exit"时退出程序
# 文件格式：
# 张三,25
# 李四,30
# 王五,28
'''
name=input('请输入人名：(输入exit退出）')
while name!='exit':
    age=input('请输入年龄：')
    print('信息已保存！')
    name = input('请输入人名：(输入exit退出）')
    with open ("users.txt", "a") as file:
        file.write(f'{name},{age}\n')
while name=='exit':
    with open("users.txt", "r") as file:
        print(file.read())
    break

with open("users.txt", "w") as file:
    file.write("")'''

#修正
while True:#(*)
    name = input('请输入人名（输入exit退出）：')
    if name == 'exit':
        break  # 先判断是否退出

    age = input('请输入年龄：')

    with open("users.txt", "a") as file:
        file.write(f'{name},{age}\n')  # 立即保存当前信息

    print('信息已保存！')

