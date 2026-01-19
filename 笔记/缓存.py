#@lru_cache(maxsize=None) 是 Python 的装饰器，用来实现记忆化搜索，也叫缓存。可以记住函数已算的结果，避免超时！
from functools import lru_cache

@lru_cache(maxsize=None)  # 加上这个装饰器
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)
print(fib(40))  # 很快！自动记住已经算过的结果