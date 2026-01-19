mod=1000000007
def fib(n):
    if n == 1 or n == 2:
        return 1
    a, b = 1, 1
    for _ in range(n - 2):
        a, b = b%mod, (a + b)%mod
    return b
t = int(input())
print(fib(t))
