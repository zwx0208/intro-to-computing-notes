a=int(input())
print(oct(a)[2:])


ei=[]
while a>0:
    ei.append(a%8)
    a//=8
ei.reverse()
print(int(''.join(map(str,ei))))


result = ''
while ei:
    result += str(ei.pop())
print(result)
