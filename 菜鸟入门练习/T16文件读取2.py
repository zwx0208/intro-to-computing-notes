# 要求：分析users.txt，找出：
# 1. 最年长的人和信息
# 2. 最年轻的人和信息
# 3. 年龄分布（<30岁，≥30岁各多少
age_s=0
age_b=0
oldest_age = 0
youngest_age = 100
oldest_person = ""
youngest_person = ""
with open('users.txt','r') as file:
    for line in file:
        line=line.strip()
        if line:
            parts=line.split(',')
            name=parts[0]
            age=int(parts[1])
        if age<30:
            age_s+=1
        else:
            age_b+=1
        if age > oldest_age:
            oldest_age = age
            oldest_person = name
        if age < youngest_age:
            youngest_age = age
            youngest_person = name

print(f'小于等于30：{age_s}人，大于等于30：{age_b}人')
print(f'最年长：{oldest_person} {oldest_age}岁')
print(f'最年轻：{youngest_person} {youngest_age}岁')
