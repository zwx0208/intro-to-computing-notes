def find(li):
    s=len(li)
    i=s-2
    while li[i]>=li[i+1] and i>=0:  #列表的负索引也存在，要及时停止循环
        i-=1
    if i>=0:
        j=s-1
        while li[j]<=li[i]:
            j-=1
        li[i],li[j]=li[j],li[i]
        lis=li[:i+1]+list(reversed(li[i+1:]))   #reversed() 返回的是反向迭代器，不能直接和列表相加。需要转成列表：
    else:
        lis=list(reversed(li))
    return lis
def main():
    m=int(input())
    for _ in range(m):
        n,k=map(int,input().split())
        li=list(map(int,input().split()))
        for _ in range(k):
            li=find(li[:])
        print(*li)
if __name__=='__main__':
    main()

