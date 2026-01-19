n=int(input())
count=0
for _ in range(n):
    sentence=input().strip().split()
    inner=False
    for word in sentence:
        if word.startswith('###') and not inner:
            count+=1
        inner=word.endswith('###')
print(count)