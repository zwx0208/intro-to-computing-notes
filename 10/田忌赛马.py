import sys
def tianji(t_horse,k_horse,n):
    t_horse.sort(reverse=True)
    k_horse.sort(reverse=True)
    money=0
    t_left,t_right=0,n-1
    k_left,k_right=0,n-1
    for _ in range(n):
        if t_horse[t_left] >k_horse[k_left]:
            t_left += 1
            k_left += 1
            money += 200
        elif t_horse[t_left] <k_horse[k_left]:
            t_right -= 1
            k_left += 1
            money -= 200
        else:
            if t_horse[t_right]>k_horse[k_right]:
                t_right -= 1
                k_right -= 1
                money += 200
            else:
                if t_horse[t_right] < k_horse[k_left]:
                    money-=200
                t_right -= 1
                k_left += 1

    return money
data=sys.stdin.read().strip().split()
idx=0
result=[]
while idx<len(data):
    n=int(data[idx])
    idx+=1
    if n==0:
        break
    t_horse=list(map(int,data[idx:idx+n]))
    idx+=n
    k_horse=list(map(int,data[idx:idx+n]))
    idx+=n
    result.append(str(tianji(t_horse,k_horse,n)))
print('\n'.join(result))