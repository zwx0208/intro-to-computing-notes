n=int(input())
m=0
for i in reversed(range(2,int(n**0.5)+1)):
    while n%i==0:
        m=n//i
        break
print(m)