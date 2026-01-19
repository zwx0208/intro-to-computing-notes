n,d=map(int,input().split())
students=sorted(list(map(int,input().split())))
found=True
for i in range(0,2*n,2):
        if students[i+1]-students[i]>d:
            found=False
            break
print('Yes'if found else 'No')



