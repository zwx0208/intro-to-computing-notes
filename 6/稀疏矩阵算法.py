import sys

data=sys.stdin.read().strip().split()
idx=0
n=int(data[idx])
idx+=1
m1 = int(data[idx])
idx += 1
m2 = int(data[idx])
idx += 1

X_triples = []
for _ in range(m1):
    r = int(data[idx])
    idx += 1
    c = int(data[idx])
    idx += 1
    v = int(data[idx])
    idx += 1
    X_triples.append((r, c, v))

Y_by_row = {}
for _ in range(m2):
    r = int(data[idx])
    idx += 1
    c = int(data[idx])
    idx += 1
    v = int(data[idx])
    idx += 1
    if r not in Y_by_row:
        Y_by_row[r] = []
    Y_by_row[r].append((c, v))

Z = {}
for i, k, xval in X_triples:
    if k in Y_by_row:
        for j, yval in Y_by_row[k]:
            key = (i, j)
            Z[key]=Z.get(key,0)+xval*yval

for (i, j), val in sorted(Z.items()):
    print(f"{i} {j} {val}")


