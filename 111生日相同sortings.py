n = int(input())
students = []
for _ in range(n):
    data=input().split()
    students.append((data[0], int(data[1]), int(data[2])))
students.sort(key=lambda x:(x[1],x[2]))

i=0
while i<len(students):
    current_date=(students[i][1],students[i][2])
    same_birthday=[]
    while i<len(students)and(students[i][1],students[i][2])==current_date:
        same_birthday.append(students[i][0])
        i+=1
    if len(same_birthday)>1:
        print(f"{current_date[0]} {current_date[1]} "+" ".join(same_birthday))

#循环语句好题，值得反复品味