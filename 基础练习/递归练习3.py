# 要求：用递归反转字符串
# 示例：
# 输入："hello" → 输出："olleh"
# 输入："a" → 输出："a"
# 输入："" → 输出：""

def reverse_string(s):
    if len(s)<=1:
        return s
    return reverse_string(s[1:]) + s[0]



print(reverse_string("hello"))
print(reverse_string("a"))
print(reverse_string(""))