# 要求：创建一个函数，接收文件名（字符串）
# 返回文件的扩展名（不带点），如果没有扩展名返回"无"
# 示例：
# 输入："document.pdf" → 返回："pdf"
# 输入："image.jpg" → 返回："jpg"
# 输入："no_extension" → 返回："无"
def document():
    name=input('输入文件名：')
    parts=name.split('.')
    if len(parts) > 1:
        extension = parts[-1]
    else:
        extension = "无"
    print(extension)
document()