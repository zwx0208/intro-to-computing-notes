n=int(input())
def find(x):
    res=[[]]
    for l in x:
        res+=[i+[l] for i in res]   #定义find(x)找到了四个数集合的所有子集
    return res
for _ in range(n):
    L=list(map(int,input().split()))
    if sum(L)<24 or sum(L)%2!=0:
        print('NO')
        continue
    subjects=find(L)
    count=0
    for r in subjects:
        if sum(r)==(sum(L)-24)//2:
            count+=1
    if count>0:
        print('YES')
    else:
        print('NO')

'''设 S=a+b+c+d（所有数的和）
当我们给某些数分配负号时，总和的变化是减去两倍的这些数的和。
即 S−2×(被选为负数的那些数的和)=24
所以问题转化为：是否存在一个子集，其元素和为 t
使得S-2t=24,即t=(S-24)*1/2'''
