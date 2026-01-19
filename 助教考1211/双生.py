x=int(input())
shuangsheng=[]
n=65536
is_prime = [True] * (n+ 1)
is_prime[0] =is_prime[1]= False
for i in range(2, int(n**0.5)+1):
    if is_prime[i]:
        for j in range(i**2, n+1, i):
            is_prime[j] = False
primes= [p for p in range(3, 65537) if is_prime[p]]
seen=set()
for p in primes:
    bin_str=bin(p)[2:]
    r_bin=bin_str[::-1]
    r_num=int(r_bin,2)
    if r_num <=n and is_prime[r_num]:
        pair=(min(r_num,p),max(r_num,p))
        if pair not in seen:
            seen.add(pair)
            shuangsheng.append(pair)
shuangsheng.sort(key=lambda m:m[0])
print(*shuangsheng[x])