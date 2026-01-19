s=list(input())
S=[]
i=0
a=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
A=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
while i<len(s):
    if s[i] in a:
        S.append(s[i].upper())
    elif s[i] in A:
        S.append(s[i].lower())
    else:
        S.append(s[i])
    i+=1
print(str(''.join(S)))

#内置函数
print(input().swapcase())
#判断
s = input()
result = ""
for char in s:
    if char.islower():
        result += char.upper()
    elif char.isupper():
        result += char.lower()
    else:
        result += char
print(result)