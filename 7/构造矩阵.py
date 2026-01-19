M=int(input())
def solve():
    n,m=map(int,input().split())
    if m==1:
        print(0)
    elif n>m-1:
        print(m)
    else:
        print(n+1)
    for i in range(min(m-1,n)):
        for j in range(m):
            print((j+i)%m,end=' ')
        print()
    if n>m-1:
        for i in range(m-1,n):
            for j in range(m):
                print(j,end=' ')
            print()
for _ in range(M):
    solve()

'''print()用法:
print(内容, end=' ')：输出内容+空格，不换行
print()：什么都不输出，只换行
print(内容)：输出内容+换行
'''