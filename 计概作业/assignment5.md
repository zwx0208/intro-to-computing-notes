# Assignment #5: 20251009 cs101 Mock Exam寒露第二天

Updated 1651 GMT+8 Oct 9, 2025

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

### E29895: 分解因数

implementation, http://cs101.openjudge.cn/practice/29895/



思路：
这个题应该说一句因数不包括他自己，不过不说也能理解就是了，思路就是倒过来找因数。
看了题解，发现不用倒过来排序，直接用if即可，我大概是被第一次的错误思路拐远了。


代码
```python
n=int(input())
m=0
for i in reversed(range(2,int(n**0.5)+1)):
    while n%i==0:
        m=n//i
        break
print(m)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![alt text](7e1e3f7bdff46fccefb815e9450ba35e.png)




### E29940: 机器猫斗恶龙

greedy, http://cs101.openjudge.cn/practice/29940/



思路：
这是典型的简单的贪心，记录最低点即可。
看了题解，我竟然跟题解一模一样。


代码

```python
n=int(input())
M=list(map(int,input().split()))
b,c=0,0
for i in range(n):
    c+=M[i]
    if c<=b:
        b=c
print(-b+1)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![alt text](555a8befdc7e438606fb9f3bd32f7b60.png)




### M29917: 牛顿迭代法

implementation, http://cs101.openjudge.cn/practice/29917/



思路：一开始没看懂是以为函数是y=x**0.5,看懂函数式后要做的就是处理不定行输入，学会了sys.stdin。这个要注意一定要加绝对值，因为是从两边逼近的。
看了题解，思路一致，理解题意真的很重要！



代码

```python
import sys
for line in sys.stdin:
    a=float(line)
    x=1.0
    count=0
    while True:
        count+=1
        x1=0.5*(x+a/x)
        if abs(x1-x)<=1e-6:
            break
        x=x1
    print(f'{count} {x1:.2f}')
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![alt text](4ea7473f1d0ccda7db8a7161ed0b95e2.png)




### M29949: 贪婪的哥布林

greedy, http://cs101.openjudge.cn/practice/29949/


思路：这是一个贪心题，有点像加强版的twins，排序之后从大吃到小，这次没有设置那种太短的变量因为真的看不懂。
看了题解，思路很好，拆成小单位使代码长度明显变短，ds说这样可能会导致内存太大，我觉得有一定道理但提交并无问题，这个列表不算太长。



代码

```python
N,M=map(int,input().split())
tval=0
remain=M
item=[]
for _ in range(N):
    v,w=map(int,input().split())
    val=v/w
    item.append((val,v,w))
item.sort(reverse=True)
for unit_val,total_v,total_w in item:
    if remain>=total_w:
        tval+=total_v
        remain-=total_w
    else:
        tval+=unit_val*remain
        break
print(f'{tval:.2f}')
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![alt text](80355c172e3ebecaffb50b948d5adcbb.png)




### M29918: 求亲和数

implementation, http://cs101.openjudge.cn/practice/29918/



思路：
这个我是先写函数然后算出区间内的所有值，再判断有无亲和数的，感觉还好。看到群里有很多同学超时了，我的方法也没有很简便，不过并没超时，而且我也不太懂为啥要讨论质因数；还有同学能背诵亲和数表，属实厉害，我之前了解过但真背不过。
看了题解，思路一致。



代码

```python
n = int(input())
def sum(x):
    if x==1:
        return 0
    total=1
    for i in range(2,int(x**0.5)+ 1):
        if x%i==0:
            total+=i
            if i!=x//i:
                total+=x//i
    return total
divisums={}
for i in range(2,n+1):
    divisums[i]=sum(i)
pairs=[]
for a in range(2,n+1):
    b=divisums[a]
    if b>a and divisums.get(b)==a:
        pairs.append((a,b))
for a,b in pairs:
    print(f"{a} {b}")
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![alt text](254afddea0976b1061c9ffbc4b92bb78.png)




### T29947:校门外的树又来了（选做）

http://cs101.openjudge.cn/practice/29947/



思路：早知道第一次写的时候就不偷懒。看了题解，觉得这个方法好，还是第一次写列表中的列表，学会了怎么处理并集的问题。



代码

```python
L, M = map(int, input().split())
intervals = []
for _ in range(M):
    m, n = map(int, input().split())
    if m > n:
        m, n = n, m
    intervals.append((m, n))
intervals.sort()

tree = []
for m, n in intervals:
    if not tree or m > tree[-1][1]:
        tree.append([m, n])
    else:
        tree[-1][1] = max(tree[-1][1], n)

cut = sum(n - m + 1 for m, n in tree)
remain = (L + 1) - cut
print(remain)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![alt text](71dab5eb87b12256970b77441da801d3.png)




## 2. 学习总结和收获

<mark>如果作业题目简单，有否额外练习题目，比如：OJ“计概2025fall每日选做”、CF、LeetCode、洛谷等网站题目。</mark>
先总结一下考试吧：1微卡，这大概就是闫老师上课说的有小问题但大家都知道的那种简单题；2很快做出，浅显的贪心；3看了十几分钟没看懂，并且深知自己不会不定行输入，skip了；4感觉比较复杂但有思路，（这时先看了眼5是个贪心，6是个原题，）就跑去写6，当时创建超长列表但好在数字小竟然过了，结果直接超内存，有点绝望；回过来写掉5，然后写了4，这时也快结束了。最终AC4，感觉对于我的垃圾水平就很正常，做的时候看见有的大佬40分钟AK了感觉很厉害。
复盘的时候感觉这种考中学挺好的（只要不发生在期末），还能早早完成作业。看了题解也受益很多，学到的知识点在整理了。




