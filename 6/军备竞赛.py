initial=int(input())
weapons=sorted(map(int,input().split()))
left=0
right=len(weapons)-1
my_count=0
enemy_count=0
while left<=right:
    if initial>=weapons[left]:
        initial-=weapons[left]
        my_count+=1
        left+=1
    elif my_count>enemy_count and left<right:
        initial+=weapons[right]
        enemy_count+=1
        right-=1
    else:
        break
print(my_count-enemy_count)