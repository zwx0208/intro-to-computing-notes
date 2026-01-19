n=int(input())
num=list(map(int,input().split()))
candy=1
candies=[1]
if n==0:
    print(0)
for i in range(1,n):
    if num[i]>num[i-1]:
        candy+=1
        candies.append(candy)
    else:
        candy=1
        candies.append(candy)
candy=1
for i in reversed(range(0,n-1)):
    if num[i]>num[i+1]:
        candy+=1
        candies[i]=max(candy,candies[i])
    else:
        candy=1
        candies[i]=max(candy,candies[i])
print(sum(candies))