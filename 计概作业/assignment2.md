# Assignment #2: 语法练习

Updated 1335 GMT+8 Sep 16, 2025

2025 fall, Complied by <mark>同学的姓名、院系</mark>



**作业的各项评分细则及对应的得分**

| 标准                                 | 等级                                                         | 得分 |
| ------------------------------------ | ------------------------------------------------------------ | ---- |
| 按时提交                             | 完全按时提交：1分<br/>提交有请假说明：0.5分<br/>未提交：0分  | 1 分 |
| 源码、耗时（可选）、解题思路（可选） | 提交了4个或更多题目且包含所有必要信息：1分<br/>提交了2个或以上题目但不足4个：0.5分<br/>少于2个：0分 | 1 分 |
| AC代码截图                           | 提交了4个或更多题目且包含所有必要信息：1分<br/>提交了2个或以上题目但不足4个：0.5分<br/>少于：0分 | 1 分 |
| 清晰头像、PDF文件、MD/DOC附件        | 包含清晰的Canvas头像、PDF文件以及MD或DOC格式的附件：1分<br/>缺少上述三项中的任意一项：0.5分<br/>缺失两项或以上：0分 | 1 分 |
| 学习总结和个人收获                   | 提交了学习总结和个人收获：1分<br/>未提交学习总结或内容不详：0分 | 1 分 |
| 总得分： 5                           | 总分满分：5分                                                |      |

>
>
>
>**说明：**
>
>1. **解题与记录：**
>
>   对于每一个题目，请提供其解题思路（可选），并附上使用Python或C++编写的源代码（确保已在OpenJudge， Codeforces，LeetCode等平台上获得Accepted）。请将这些信息连同显示“Accepted”的截图一起填写到下方的作业模板中。（推荐使用Typora https://typoraio.cn 进行编辑，当然你也可以选择Word。）无论题目是否已通过，请标明每个题目大致花费的时间。
>
>2. **课程平台：**课程网站位于Canvas平台（https://pku.instructure.com ）。该平台将在<mark>第2周</mark>选课结束后正式启用。在平台启用前，请先完成作业并将作业妥善保存。待Canvas平台激活后，再上传你的作业。
>
>3. **提交安排：**提交时，请首先上传PDF格式的文件，并将.md或.doc格式的文件作为附件上传至右侧的“作业评论”区。确保你的Canvas账户有一个清晰可见的本人头像，提交的文件为PDF格式，并且“作业评论”区包含上传的.md或.doc附件。
>
>4. **延迟提交：**如果你预计无法在截止日期前提交作业，请提前告知具体原因。这有助于我们了解情况并可能为你提供适当的延期或其他帮助。  
>
>请按照上述指导认真准备和提交作业，以保证顺利完成课程要求。





## 1. 题目

### 263A. Beautiful Matrix

implementation, 800, https://codeforces.com/problemset/problem/263/A



思路：
matrix = [input().split() for _ in range(5)]   学到了，这是获得矩阵的关键一行，input循环五次，split按空格分开，【】接收为列表。
第一次做矩阵的题，花了四十分钟，狠狠恶补矩阵的知识，代码其实还蛮方便的。

代码

```python
matrix = [input().split() for _ in range(5)]   
for i in range(5):
    for j in range(5):
        if matrix[i][j]=='1':
            print(abs(i-2)+abs(j-2))


```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![alt text](2acf6087da60087c48a5e62f8f49fa24.png)




### 1328A. Divisibility Problem

math, 800, https://codeforces.com/problemset/problem/1328/A



思路：这个还比较简单，我是按a与b大小讨论了一下，然后弄个向上取整这样的。本来是想用max和min，但后来发现写了一大串，没那个必要。



代码

```python
n=int(input())
for _ in range(n):
    a,b=(map(int,input().split()))
    c=(a+b-1)//b
    if a>b:
        print(b*c-a)
    else:
        print(b-a)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![alt text](bf07065447e4fa3e26e9fdac302e6b12.png)




### 427A. Police Recruits

implementation, 800, https://codeforces.com/problemset/problem/427/A



思路：这个简单，写个for循环遍历列表，唯一比较搞笑的是第一行输入似乎完全没用。



代码

```python
n=int(input())
case= list(map(int, input().split()))
p,c=0,0
for i in case:
    if i==-1:
        if p==0:
            c+=1
        elif p>0:
            p-=1
    else:
        p+=i
print(c)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![alt text](bb8cccc96a6f94368ef9965ddea5e2dc.png)




### E02808: 校门外的树

implementation, http://cs101.openjudge.cn/pctbook/E02808/


思路：
思路很简单，创建一个路的列表，然后有树的赋值为零，最后求和。有一个坑点我一开始搞错了，就是路的长度要加一。



代码

```python
m,n = map(int, input().split())
t=[1]*(m+1)
for _ in range(n):
    a, b = map(int, input().split())
    for j in range(a, b + 1):
        t[j]=0
print(sum(t))

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![alt text](a29a58a0b4f59566d3c00beee345049d.png)




### sy60: 水仙花数II

implementation, https://sunnywhy.com/sfbj/3/1/60



思路：
做这题发现自己蠢，思路挺简单结果最后输出int出不来，改半天才发现要转成str，提交的时候第一次还交成了C++。看了下题解差不多，但他是最后再读数据的，而且还定义了函数，我一般不定义函数因为不是很擅长函数，要恶补函数了！


代码

```python
a, b = map(int, input().split())
result=[]
for n in range(a,b+1):
    m=n//100
    i=(n//10)%10
    j=n%10
    if m**3+i**3+j**3==n:
        result.append(n)
if result:
    print(" ".join(map(str,result)))
else:
    print("NO")
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![alt text](08a6389b35735e075169294bff41a5d9.png)




### M01922: Ride to School

implementation, http://cs101.openjudge.cn/pctbook/M01922/



思路：

这个题其实我能看懂，就是算所有人到达终点的时间取最小值，也写了一个，但提交了还是不对，并且一开始还被向上取整的中文翻译骗了，不过最后还是WA。目前不太会，对我的水平有点太拔高了：（

代码

```python

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>





## 2. 学习总结和收获
学到了很多，比如矩阵的输入还有一些列表和输出的处理，发现虽然语法啃了挺久但还是很多小点不清楚，空有思路但语法稀烂有种茶壶煮饺子的感觉。现在三个作业都写完了，准备开始刷题了，因为我自己学的一堆语法一做题就使不出来，但做题的时候还学到蛮多的。


