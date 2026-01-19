n=int(input())
students=list(map(int,input().split()))
timelist=[]
Time=[]
sequence=[]
timing=0
for idx, time in enumerate(students, 1):  # 从1开始编号
    timelist.append((time, idx))
timelist.sort()
for x in timelist:
    Time.append(x[0])
    sequence.append(x[1])
print(*sequence)
count=n
for item in Time:
    timing+=item*(count-1)
    count-=1
print(f'{timing/n:.2f}')





