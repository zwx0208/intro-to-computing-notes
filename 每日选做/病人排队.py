n = int(input())
patients = []
for i in range(n):
    ID,age=input().split()
    patients.append((ID,int(age)))  #使用列表保存元组（而非字典），不会丢失输入顺序
elderly=[p for p in patients if p[1]>=60]
young=[p for p in patients if p[1]<60]
elderly.sort(key=lambda x:(-x[1]))  #使用匿名函数排序
for p in elderly:
    print(p[0])
for p in young:
    print(p[0])