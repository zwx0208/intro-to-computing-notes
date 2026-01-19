#左边右边最高的较小值-当前高度 为能接住的雨水;左右哪边矮，就先处理哪边
n=int(input())
bricks=list(map(int,input().split()))
l,r=0,n-1
lm,rm=0,0
water=0
while l<r:
    if bricks[l]<bricks[r]:
        if bricks[l]>lm:
            lm=bricks[l]
        else:
            water+=lm-bricks[l]
        l+=1
    else:
        if bricks[r]>rm:
            rm=bricks[r]
        else:
            water+=rm-bricks[r]
        r-=1
print(water)
