n=int(input())
def date(x):
    month=[0,31,28,31,30,31,30,31,31,30,31,30,31]
    days=0
    for i in range(x):
        days+=month[i]
    return days
for _ in range(n):
    cal=list(map(int,input().split()))
    day1=date(cal[0])+cal[1]
    day2=date(cal[3])+cal[4]
    b=cal[2]*2**(day2-day1)
    print(b)
