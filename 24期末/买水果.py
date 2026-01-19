from  collections import Counter

n,m=map(int,input().split())
prices=list(map(int,input().split()))
prices.sort()
fruits=[]
for _ in range(m):
    fruits.append(input())
fruits_dict=Counter(fruits)
nums=list(fruits_dict.values())
nums.sort(reverse=True)
s,b=0,0
for i in range(len(nums)):
    s+=nums[i]*prices[i]
    b+=nums[i]*prices[-i-1]
print(s,b)