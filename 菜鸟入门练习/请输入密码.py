# 要求：使用while循环实现密码验证
# 规则：
# 1. 预设密码为"python123"
# 2. 用户输入密码，最多尝试3次
# 3. 密码正确：显示"登录成功"
# 4. 密码错误：显示剩余尝试次数
# 5. 3次都错：显示"账户锁定"
password='python123'
a=0
password_user=0
while password_user!=password:
    password_user=input('请输入密码：（共三次机会）')
    if password_user!=password:
        a+=1
        print(f'密码错误，剩余{3-a}次机会！')
    if a==3:
        print('账户锁定')
        break
print('登陆成功！')
#被DS夸简洁的代码哦！