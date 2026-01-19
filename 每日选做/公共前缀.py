n=int(input())
strings=[]
for _ in range(n):
    strings.append(input())
def find(strings):
    minl=min(len(s) for s in strings)
    same=[]
    for i in range(minl):
        char=strings[0][i]
        if all(s[i]==char for s in strings):  #竟然第一次见这么用！可以用all()写for循环
            same.append(char)
        else:
            break
    return ''.join(same)
print(find(strings))