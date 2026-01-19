x=int(input())
def is_prime(n):
    if n<=2:
        return False
    for i in range(3, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
if x<6 or x%2!=0:
    print('Error!')
else:
    found=False
    for num in range(3,x//2+1,2):
        if is_prime(num) and is_prime(x-num):
            print(f'{x}={num}+{x-num}')
            found=True
    if not found:
        print('Error!')
