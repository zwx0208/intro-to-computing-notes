# 要求：创建函数检测密码强度
# 规则：
# 强密码：长度≥8，包含字母和数字
# 中密码：长度≥6，包含字母或数字
# 弱密码：其他情况
# 返回："强"、"中"、"弱"
# 示例：
# "abc12345" → "强"
# "password" → "中"
# "123" → "弱"

def check_password():
    password=input('请输入密码：')
    parts=list(password)
    if len(parts)<=6 & str.isalpha(password)==1 or str.isdigit(password)==1:
        print('弱')
    elif len(parts)>=6:
        if str.isalpha(password)==1 or str.isdigit(password)==1:
            print('中')
        elif len(parts)>=8:
            print('强')
        else:
            print('中')

check_password()

'''def check_password():
    password = input('请输入密码：')
    length = len(password)
    has_letter = any(char.isalpha() for char in password)  # 是否有字母(*)
    has_digit = any(char.isdigit() for char in password)   # 是否有数字
    
    if length >= 8 and has_letter and has_digit:
        return "强"
    elif length >= 6 and (has_letter or has_digit):
        return "中" 
    else:
        return "弱" 
'''