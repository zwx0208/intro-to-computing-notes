n,m=map(int,input().split())
battery=[tuple(map(int,input().split())) for _ in range(n)]
battery.sort(key=lambda x:(x[0]+x[1],-x[0]))
main=battery[0][0]+battery[0][1]
other=sorted(battery[1:])
rnd=m//main*2 + int(m%main>=battery[0][0])
s=0
for i in range(n - 1):
    s += other[i][0]
    if m < s or other[i][0]>=main:
        break
    rnd=max(rnd,i+1+(m-s)//main*2+int((m-s)%main>=battery[0][0]))
print(rnd)
