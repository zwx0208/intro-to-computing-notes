# Assignment #1: 自主学习

Updated 1427 GMT+8 Sep 9, 2025

2025 fall, Complied by ==郑文萱 基础医学院==



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
>4. **延迟提交：****如果你预计无法在截止日期前提交作业，请提前告知具体原因。这有助于我们了解情况并可能为你提供适当的延期或其他帮助。  
>
>请按照上述指导认真准备和提交作业，以保证顺利完成课程要求。





## 1. 题目

### E02733: 判断闰年

http://cs101.openjudge.cn/pctbook/E02733/



思路：
就是条件判断吧，要注意的点就是条件的先后，能排除先排除


代码

```python
year=int(input())
if year % 3200 == 0:
    print("N")
elif year % 100 == 0:
    if year % 400 == 0:
        print("Y")
    else:
        print("N")
elif year % 4 == 0:
    print("Y")
else:
    print("N")

```



代码运行截图 ==（至少包含有"Accepted"）==
![alt text](16ef1f685b657f0afbdd0e2fe5d3161c.png)




### E02750: 鸡兔同笼

http://cs101.openjudge.cn/pctbook/E02750/



思路：
这个只看最多和最少就是除以二或者一个除以四的向上取整，排除单数的情况就好了


代码

```python
a=int(input())
if a%2==0:
    print(f'{(a+3)//4} {a//2}')
else:
    print('0 0')
```



代码运行截图 ==（至少包含有"Accepted"）==
![alt text](f074c42a20b7ad26afbf6a38b49405a3.png)




### 50A. Domino piling

greedy, math, 800, http://codeforces.com/problemset/problem/50/A



思路：
比鸡兔同笼还简单，唯一考的点在于列表拆分和接收吧



代码

```python
a= input().split()
m = int(a[0])
n = int(a[1])
print((m * n) // 2)

```



代码运行截图 ==（至少包含有"Accepted"）==
![alt text](9cf355e0db1d533e554579783a12431d.png)




### 1A. Theatre Square

math, 1000, https://codeforces.com/problemset/problem/1/A



思路：
还是一个向上取整，n,m,a=list(map(int,input().split()))这个是做题的时候学的，很常用



代码

```python
n,m,a=list(map(int,input().split()))
print(((n+a-1)//a)*((m+a-1)//a))

```



代码运行截图 ==（至少包含有"Accepted"）==
![alt text](28d5451b41c919259e669e2dbccf720f.png)




### 112A. Petya and Strings

implementation, strings, 1000, http://codeforces.com/problemset/problem/112/A



思路：
其实做这个题之前并不知道能直接比，还以为要用列表转换过来比总和之类的，结果看了网站后面附上的维基百科后才知道是按字典里面的单词排列顺序那样的，而且竟然可以直接比较！好神奇。


代码

```python
a1 = input().strip()
a2 = input().strip()
a11 = a1.lower()
a21 = a2.lower()
if a11 < a21:
    print(-1)
elif a11 > a21:
    print(1)
else:
    print(0)

```



代码运行截图 ==（至少包含有"Accepted"）==
![alt text](616c988644a68aee012c257bed60b9fb.png)




### 231A. Team

bruteforce, greedy, 800, http://codeforces.com/problemset/problem/231/A



思路：
写个for循环统计每行的和然后判断大小，题目看起来长但其实很好理解，但bruteforce、greedy这两个tag都不是很理解。

代码

```python
n = int(input())   
count = 0
for _ in range(n):
    a, b, c = map(int, input().split())
    if a + b + c >= 2:
        count += 1
print(count)

```



代码运行截图 ==（至少包含有"Accepted"）==
![alt text](148aad27ccae82318ca6b110a396473d.png)




## 2. 学习总结和收获
零基础，先做完assignment3后反过来做1，好简单啊（记得当时刚上课的时候点开感觉都没啥思路的）。不过这只是掌握最基本的语法，之后的题目一定要加强思维了！



