s = input().strip()
result = []
current_num = ""  #l两个接收器，一个字符串不断归零，一个列表接收字符串
for char in s:
    if char.isdigit():
        current_num += char
    else:
        if current_num:
            num=str(int(current_num))
            result.append(num)
            current_num = ""
if current_num:   #最后一组也要输出
    num = str(int(current_num))
    result.append(num)
for num in result:
    print(num)
