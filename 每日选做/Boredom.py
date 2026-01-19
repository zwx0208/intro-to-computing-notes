n=int(input())
a=list(map(int,input().split()))
a.sort()
l=a[0]
r=a[-1]
nums=[0]*(r+1)
for item in a:
        nums[item]+=item
dp=[0]*(r+1)
for j in range(l,r+1):
    dp[j]=max(dp[j-1],dp[j-2]+nums[j])
print(dp[r])
