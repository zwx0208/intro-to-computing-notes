n=int(input())
def  taibonaqi(i):
    if i==0:
        return 0
    elif i==1 or i==2:
        return 1
    else:
        return taibonaqi(i-1)+taibonaqi(i-2)+taibonaqi(i-3)
print(taibonaqi(n))