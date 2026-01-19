friends = {"小明": 18, "小红": 17, "小刚": 19}
name=input('请输入朋友名字')
age=friends.get(name)
print(f'{name}的年龄是：{age}')
if friends.get(name) is None:
    friends[name]=int(input('请输入新朋友的年龄'))
