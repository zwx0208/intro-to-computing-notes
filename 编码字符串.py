string=list(input().lower())
string.append('1')
output=[]
count=1
for i in range(1,len(string)):
    if string[i]!=string[i-1]:
        output.append(f'({string[i-1]},{count})')
        count=1
    elif string[i]==string[i-1]:
        count+=1
print(''.join(output))

# 可以最后再处理最后一组：result.append(f"({s[-1]},{count})")


