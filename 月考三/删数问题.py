n=list(map(int,input()))
k=int(input())
idx=0
output=[]
while len(n)-k>0:
    minwei = float('inf')
    for item in n[idx:k+1]:
        if item<minwei:
            idx=n.index(item,idx)
            minwei=item
    k+=1
    idx+=1
    output.append(str(minwei))
print(int(''.join(output)))





