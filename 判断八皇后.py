matrix=[list(map(int,input().split())) for _ in range(8)]
place=[]
for i in range(8):
    for j in range(8):
        if matrix[i][j]==1:
            place.append([i,j])
find=False
for m in range(8):
    for item in place[m+1:]:
        if sum(item)==sum(place[m]) or item[0]==place[m][0] or item[1]==place[m][1]:
            find=True
            break
print('NO' if find else 'YES')
