# Assignment #4: T-primes + 贪心

Updated 1814 GMT+8 Sep 30, 2025

2025 fall, Complied by <mark>郑文萱 基础医学院</mark>



>**说明：**
>
>1. **解题与记录：**
>
>  对于每一个题目，请提供其解题思路（可选），并附上使用Python或C++编写的源代码（确保已在OpenJudge， Codeforces，LeetCode等平台上获得Accepted）。请将这些信息连同显示“Accepted”的截图一起填写到下方的作业模板中。（推荐使用Typora https://typoraio.cn 进行编辑，当然你也可以选择Word。）无论题目是否已通过，请标明每个题目大致花费的时间。
>
>2. 提交安排：**提交时，请首先上传PDF格式的文件，并将.md或.doc格式的文件作为附件上传至右侧的“作业评论”区。确保你的Canvas账户有一个清晰可见的本人头像，提交的文件为PDF格式，并且“作业评论”区包含上传的.md或.doc附件。
> 
>4. **延迟提交：**如果你预计无法在截止日期前提交作业，请提前告知具体原因。这有助于我们了解情况并可能为你提供适当的延期或其他帮助。  
>
>请按照上述指导认真准备和提交作业，以保证顺利完成课程要求。





## 1. 题目

### 34B. Sale

greedy, sorting, 900, https://codeforces.com/problemset/problem/34/B



思路：
这个应该不算贪心题，只需排序然后尽可能地取负数就行。


代码

```python
n,m=map(int, input().split())
prices=list(map(int, input().split()))
prices.sort()
print(sum(-x for x in prices[:m] if x<0))

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![alt text](7d905abfeff6d5c3be771d5aed378a07.png)




### 160A. Twins

greedy, sortings, 900, https://codeforces.com/problemset/problem/160/A



思路：
倒序排序然后累加直到和大于总和的一半即可，一开始忘记用计数器写了个循环结果一直循环print一堆数而不是最小的那个，有点低级的错误。


代码

```python
n=int(input())
coins=list(map(int, input().split()))
S=sum(coins)
coins.sort(reverse=True)
s=0
count=0
for i in coins:
    s+=i
    count+=1
    if s>S/2:
        break
print(count)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![alt text](b9c2110e4ac38876faa3ef0af683ca21.png)




### 1879B. Chips on the Board

constructive algorithms, greedy, 900, https://codeforces.com/problemset/problem/1879/B



思路：
这个看题看了好久才懂，其实解法没有那么复杂，题目给的那个3*3方格更是障眼法。我觉得喜欢玩数独或者象棋的朋友更容易理解，就相当于每个格子都统管所在的行和列，覆盖完整棋盘就可以，要么所有行被选中要么所有列被选中，那么就比较sum(a)+n*min(b)与n*min(a)+sum(b)谁最小就可以了。另外，这次（好像？）还是第一次在作业里面用sys，我目前刷的题都比较简单没有那么多样例，但以后可能会经常遇到这种很多输入的，所以要记住data=sys.stdin.read().split()这种读取方式。



代码

```python
import sys
data=sys.stdin.read().split()
n=int(data[0])
idx=1
results=[]
for _ in range(n):
    n=int(data[idx]);idx+=1
    a=list(map(int,data[idx:idx + n]));idx+=n
    b=list(map(int,data[idx:idx + n]));idx+=n
    res = min(sum(a)+n*min(b),n*min(a)+sum(b))
    results.append(str(res))
print("\n".join(results))
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![alt text](1d35034ce838d3ef61410b4f5145b142.png)




### M01017: 装箱问题

greedy, http://cs101.openjudge.cn/pctbook/M01017/


思路：
此题跟taxi好像（后来又独立把taxi做出来了），但是讨论的更多。上题的sys继续运用了一下，讨论其实没啥好说的，就很繁琐但也没办法，而且中间变量好多特别需要记住变量的含义，我个人又比较喜欢设置很短的变量名所以就还挺需要用纸记一下的，而且在纸上画一下格子也会好想一点。


代码

```python
import sys
for line in sys.stdin:
    a1,a2,a3,a4,a5,a6=map(int,line.split())
    if a1==a2==a3==a4==a5==a6==0:
        break
    boxes=a6+a5+a4+(a3+3)//4
    s1=a5*11
    s2=a4*5
    r3=a3%4
    extra_s1=0
    if r3==1:
        s2+=5
        extra_s1=7
    elif r3==2:
        s2+=3
        extra_s1=6
    elif r3==3:
        s2+=1
        extra_s1=5
    s1+=extra_s1
    if a2<=s2:
        s1+=(s2-a2)*4
        a2=0
    else:
        a2-=s2
        boxes+=(a2+8)//9
        if a2%9!=0:
            s1+=(9-(a2%9))*4
    a1-=s1
    if a1>0:
        boxes+=(a1+35)//36
    print(boxes)

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![alt text](7bf2f2c26ba0b32a166f745c27982a8c.png)




### M01008: Maya Calendar

implementation, http://cs101.openjudge.cn/practice/01008/



思路：
我的思路是先把h历法转换成总天数，再把总天数转换成t历法，中间很多小细节要注意，比如我写的时候就笔误打错了，然后RE，非常痛苦地找了半天，代码长的时候真的很难找！


代码

```python
n=int(input())
print(n)
H=["pop","no","zip","zotz","tzec","xul","yoxkin","mol","chen","yax","zac","ceh","mac","kankin","muan","pax","koyab","cumhu","uayet"]
T=["imix","ik","akbal","kan","chicchan","cimi","manik","lamat","muluk","ok","chuen","eb","ben","ix","mem","cib","caban","eznab","canac","ahau"]
for i in range(n):
    date=input().split()
    day=int(date[0].strip('.'))
    month=date[1]
    year=int(date[2])
    monthi=H.index(month)
    days=year*365+monthi*20+day

    Tyear=days//260
    Tday=days%260
    number=(Tday%13)+1
    namei=Tday%20
    name=T[namei]
    print(f"{number} {name} {Tyear}")
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![alt text](87ce75f5937ea6e02e0adcaa8939326a.png)




### 230B. T-primes（选做）

binary search, implementation, math, number theory, 1300, http://codeforces.com/problemset/problem/230/B



思路：T-primes就是质数的乘方，用的埃氏筛竟然没超时！（其实是因为我只会埃氏筛，其他的都没用过）



代码

```python
def sieve(n):
    is_prime=[True]*(n+1)
    is_prime[0]=is_prime[1]=False
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i,n+1,i):
                is_prime[j]=False
    return is_prime
def main():
    n=int(input())
    numbers=list(map(int, input().split()))
    is_prime=sieve(10**6)
    for n in numbers:
        r=int(n**0.5)
        if r**2==n and is_prime[r]==1:
            print("YES")
        else:
            print("NO")
main()
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![alt text](89014fbd974a733df1acfd543774a2bc.png)




## 2. 学习总结和收获
理解了闫老师上课说的贪心题要么太简单，要么太套路，要么太难，这次作业就很好的诠释了这句话。收获比较大的就是对贪心的认知加深了，以及学会了埃氏筛。最近自己在练递归，还试了试汉诺塔，感觉自相似真的很奇妙啊，跟高中的时候做的函数递推式的思路很像（比如马尔科夫链）。不过我做的都是AI给我出的小练习，还没有太多的运用到实战，希望刷更多的题吧。





