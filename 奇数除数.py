n=int(input())
for _ in range(n):
    num=int(input())
    s=str(bin(num))
    if '1' in s[3:]:
        print('YES')
    else:
        print('NO')