def main():
    n,m=map(int,input().split())
    days=[int(input()) for _ in range(n)]
    l=max(days)
    r=sum(days)
    def cover(maxcost):
        count=1
        nowspend=0
        for d in days:
            if nowspend+d<=maxcost:
                nowspend+=d
            else:
                count+=1
                nowspend=d
        return count<=m
    while l<r:
        mid=(r+l)//2
        if cover(mid):
            r=mid
        else:
            l=mid+1
    print(l)
if __name__=='__main__':
    main()