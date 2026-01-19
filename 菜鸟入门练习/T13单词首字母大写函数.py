# 要求：创建函数，接收一个句子
# 将每个单词的首字母转为大写，其余字母小写
# 示例：
# 输入："hello world" → 返回："Hello World"
# 输入："PYTHON IS FUN" → 返回："Python Is Fun"



def function():
    sentence=input('请输入语句：')
    parts=sentence.split(' ')
    parts_title=[str.title(part) for part in parts]
    sentence_1=' '.join(parts_title)  # 用空格连接(*)
    print(sentence_1)
function()


# 连接符.join(列表)
'-'.join(['a', 'b', 'c'])    # 'a-b-c'
' '.join(['Hello', 'World']) # 'Hello World'
''.join(['H', 'e', 'l', 'l', 'o'])  # 'Hello'（无间隔）
'\n'.join(['line1', 'line2']) # 换行连接




