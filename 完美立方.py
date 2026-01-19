n=int(input())
cubes=[i**3 for i in range(n+1)]
answer=[]
for a in range(6,n+1):
    a3=cubes[a]
    for b in range(2,a):
        b3=cubes[b]
        for c in range(b,a):
            c3=cubes[c]
            d3=a3-b3-c3
            if d3 in cubes and cubes.index(d3)>c:
                d=cubes.index(d3)
                answer.append((a,b,c,d))
answer.sort()
for a,b,c,d in answer:
    print(f'Cube = {a}, Triple = ({b},{c},{d})')




