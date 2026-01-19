n=int(input())
drinks=list(map(int,input().split()))
m=0
for i in range(n):
    m+=drinks[i]/100
print(f'{m/n*100:.12f}')