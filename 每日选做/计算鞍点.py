matrix=[list(map(int,input().split())) for _ in range(5)]
found=False
for i in range(5):
    vmax=matrix[i][0]
    lmax=0
    for j in range(1,5):
        if matrix[i][j]>vmax:
            vmax=matrix[i][j]
            lmax=j
    an=True
    for m in range(5):
        if matrix[m][lmax]<vmax:
            an=False
            break
    if an:
        print(f'{i+1} {lmax+1} {vmax}')
        found=True
        break
if not found:
    print('not found')

