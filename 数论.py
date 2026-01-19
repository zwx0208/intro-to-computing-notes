def pFactors(n):
    from math import sqrt
    pFact, limit, check, num = [], int(sqrt(n)) + 1, 2, n
    for check in range(2, limit):
        while num % check == 0:
            pFact.append(check)
            num/=check
    if num > 1:
        pFact.append(num)
    return pFact
n=int(input())
def M(n):
    if n==1:
        return 1
    pass
    fact=pFactors(n)
    for item in fact:
        if fact.count(item)>1:
            return 0
        else:
            if len(fact)%2==0:
                return 1
            else:
                return -1
print(M(n))