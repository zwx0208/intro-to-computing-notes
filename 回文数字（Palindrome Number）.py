import sys
for line in sys.stdin:
    num_str=line.strip()
    if num_str==num_str[::-1]:
        print("YES")
    else:
        print("NO")

