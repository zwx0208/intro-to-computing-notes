n=int(input())
boys=sorted(list(map(int,input().split())))
m=int(input())
girls=sorted(list(map(int,input().split())))
dp=[[0]*(n+1) for _ in range(m+1)]   #避免索引越界的常用手段————创建更大的列表
for i in range(1,m+1):
    for j in range(1,n+1):
        if abs(girls[i-1]-boys[j-1])<=1:
            dp[i][j]=max(dp[i-1][j-1]+1,dp[i][j-1])
        else:
            dp[i][j]=max(dp[i-1][j],dp[i][j-1])
print(dp[m][n])



#贪心也很简单（同向双指针）
n = int(input())
boys = sorted(list(map(int, input().split())))
m = int(input())
girls = sorted(list(map(int, input().split())))
i = j = count = 0
while i < n and j < m:
    if abs(boys[i] - girls[j]) <= 1:
        count += 1
        i += 1
        j += 1
    elif boys[i] < girls[j]:
        i += 1
    else:
        j += 1
print(count)