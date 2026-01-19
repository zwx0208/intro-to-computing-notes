t=int(input())
for _ in range(t):
    e,f=map(int,input().split())
    total_weight=f-e
    n=int(input())
    coins=[]
    for _ in range(n):
        p,w=map(int,input().split())
        coins.append((p,w))
    dp=[float('inf')]*(total_weight+1)
    dp[0]=0
    for p,w in coins:
        for weight in range(w,total_weight+1):
            if dp[weight-w]!=float('inf'):
                dp[weight]=min(dp[weight-w]+p,dp[weight])
    if dp[total_weight]==float('inf'):
        print('This is impossible.')
    else:
        print(f'The minimum amount of money in the piggy-bank is {dp[total_weight]}.')
