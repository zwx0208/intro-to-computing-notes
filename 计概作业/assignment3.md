# Assignment #3: 语法练习

Updated 1440 GMT+8 Sep 23, 2025

2025 fall, Complied by <mark>郑文萱，基础医学院</mark>



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

### E28674:《黑神话：悟空》之加密

http://cs101.openjudge.cn/pctbook/E28674/



思路：
这个题似乎是咱班助教出的（？）
思路比较清楚，用一个列表接收然后取余运算，但有坑：小写和大写要分开处理，密钥到铭文不是往后而是往前，很有意思的题目！


代码

```python
k = int(input().strip())
s = input().strip()
upper_alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower_alpha = "abcdefghijklmnopqrstuvwxyz"
result = []
for c in s:
    if c in upper_alpha:
        idx = upper_alpha.index(c)
        idx1 = (idx - k % 26 + 26) % 26
        result.append(upper_alpha[idx1])
    elif c in lower_alpha:
        idx = lower_alpha.index(c)
        idx1 = (idx - k % 26 + 26) % 26
        result.append(lower_alpha[idx1])
    else:
        result.append(c)
print(''.join(result))
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![alt text](3595ad8a606280f5945ec1f0f13580d4.png)




### E28691: 字符串中的整数求和

http://cs101.openjudge.cn/pctbook/E28691/



思路：
这个好简单，只需要按空格分开然后取前两位就可以了。


代码

```python
s1, s2 = input().split()
num1 = int(s1[:2])
num2 = int(s2[:2])
print(num1+num2)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![alt text](45c429e7ce03f5d9df196ac88ad73917.png)




### M28664: 验证身份证号 

http://cs101.openjudge.cn/pctbook/M28664/



思路：这个思路很清楚，创建列表然后乘对应位置的值再相加后取余验证。



代码

```python
n = int(input().strip())
factors = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
check_codes = ['1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2']

for _ in range(n):
    id_card = input().strip()
    front_17 = id_card[:17]
    last = id_card[17]

    total = 0
    for i in range(17):
        total += int(front_17[i]) * factors[i]

    id1 = total % 11
    correct_check = check_codes[id1]

    if correct_check == last:
        print("YES")
    else:
        print("NO")
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![alt text](2f1f95ada25af4917b4467f8285c701e.png)




### M28678: 角谷猜想

http://cs101.openjudge.cn/pctbook/M28678/


思路：非常简单啊，一个循环就可以了，不过以后变量设置尽量搞成a这种的（还是经验不足），不然太繁琐了，看起来也很长似的。唯一要注意的是要整除否则会显示浮点数。



代码

```python
number=int(input())
while number>1:
    if number%2==0:
        print(f'{number}/2={number//2}')
        number//=2
    else:
        print(f'{number}*3+1={number*3+1}')
        number=number*3+1
print('End')

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![alt text](844dce0d51e4fd5b093702923a99e183.png)




### M28700: 罗马数字与整数的转换

http://cs101.openjudge.cn/pctbook/M28700/



思路：这个不会，好复杂



代码

```python

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>





### 158B. Taxi

*special problem, greedy, implementation, 1100,  https://codeforces.com/problemset/problem/158/B



思路：哇，竟然是贪心算法（研究了半个小时仍旧写不出来，按理说四个人其实不算太大，下次一定！）



代码

```python

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>





## 2. 学习总结和收获

<mark>如果作业题目简单，有否额外练习题目，比如：OJ“计概2025fall每日选做”、CF、LeetCode、洛谷等网站题目。</mark>
我是零基础，自开课以来一直没敢做作业，一直在不停和AI对话学语法（学了快200次对话的语法），把菜鸟教程看完了，还看了几本其他书的语法部分，后来发现做题还是不行就和AI对话让它出题我做，顺便复习语法。
这是我独立完成的第一个作业（准备先做3再补12），感觉有的题比想象中简单很多！（不过还是有题不会，感觉是数学也要加强）
还有每日选做暂时没做太多，只挑了一开始800的，最近还是想巩固一下语法然后完成作业，开始刷题了之后会补上的。




