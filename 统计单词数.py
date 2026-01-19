'''from soupsieve.util import lower
word=lower(' '+str(input()).strip()+' ')
passage=lower(' '+str(input()).strip()+' ')
if word not in passage:
    print(-1)
else:
    word=word.strip()
    passage=list((passage.strip()).split())
    count=passage.count(word)
    print(f'{count} {passage.index(word)}
#strip()很重要，尤其是字符串之中，否则可能有怪东西混进来'''

target_word = input().strip().lower()
text = input().strip()
words = text.lower().split()

if target_word not in words:
    print(-1)
else:
    count = words.count(target_word)

    first_index = words.index(target_word)
    words_before = words[:first_index]

    position = 0
    for word in words_before:
        position += len(word) + 1
    print(f"{count} {position}")

    #MD此题太恶心了，我服了做了一个多小时烦人死了,先看错题后又不停WA.太坑了这空格胡来呢，根本不是规范的文章！