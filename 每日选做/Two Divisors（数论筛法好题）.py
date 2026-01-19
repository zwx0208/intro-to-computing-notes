n=int(input())
a=list(map(int,input().split()))
#线性筛法预处理
MAX=10**7+1
spf=list(range(MAX))  #最小质因子
primes=[]
for i in range(2,MAX):
    if spf[i]==i:
        primes.append(i)
    for p in primes:
        if p*i>=MAX or p>spf[i]:
            break
        spf[p*i]=p
out1=[]
out2=[]
for num in a:
    p=spf[num]
    temp=num
    while temp%p==0:
        temp//=p
    if temp==1:
        out1.append(-1)
        out2.append(-1)
    else:
        out1.append(p)
        out2.append(temp)
print(' '.join(map(str,out1)))
print(' '.join(map(str,out2)))   #注意改为字符串格式