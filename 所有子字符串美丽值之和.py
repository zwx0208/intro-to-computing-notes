from collections import Counter
s = "aabcb"
ans, n = 0, len(s)
for i in range(n):
    cnt = Counter()  #创建了一个统计字母的字典
    for j in range(i, n):
        cnt[s[j]]+=1
        ans+=max(cnt.values())-min(cnt.values())
print(ans)