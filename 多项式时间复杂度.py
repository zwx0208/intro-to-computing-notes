arr=list(input().strip().split('+'))
flag=0
for item in arr:
    item_new=list(item.split("n^"))
    if item_new[0]!='0' and int(item_new[1])>flag:
        flag=int(item_new[1])
print(f'n^{flag}')