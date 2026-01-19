n,m=map(int,input().split())
con=[]
for _ in range(n):
    score=list(map(int,input().split()))
    score.sort()
    con.append(f'{sum(score[1:m-1])/(m-2):.2f}')
con.sort()
print(con[-1])