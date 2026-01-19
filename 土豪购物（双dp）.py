goods=list(map(int,input().split(',')))
n=len(goods)
f=goods[0]
g=float('-inf')
ans=goods[0]
for i in range(1,n):
    new_g=max(f,g+goods[i])
    new_f=max(f+goods[i],goods[i])
    f,g=new_f,new_g
    ans=max(ans,f,g)
print(ans)

'''维护两个dp:f,g
f指的是不删除的包含当前元素的连续最大
g指的是可删除的包含当前元素的连续最大
f的状态转移方程：f[i]=max(f[i-1]+goods[i],goods[i])  经典的连续最大kadane算法
g的状态转移方程：g[i]=max(f[i-1],g[i-1]+goods[i])  删了当前的和之前就删了，需要依赖f
由于状态i只取决于i-1，所以只用存两个，滚动数组优化
'''