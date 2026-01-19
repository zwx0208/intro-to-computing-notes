# 要求：创建一个函数，接收邮箱地址
# 返回邮箱的域名（@后面的部分）
# 如果没有@或格式错误，返回"无效邮箱"
# 示例：
# 输入："user@example.com" → 返回："example.com"
# 输入："invalid.email" → 返回："无效邮箱"
def address_handle():
    address=input('请输入邮箱地址：')
    parts=address.split('@')
    if len(parts)>1:
        return parts[-1]
    else:
        return '无效邮箱'
print(address_handle())