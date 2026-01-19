q = int(input())
for _ in range(q):
    n = int(input())
    arr = list(map(int, input().split()))

    freq = {}
    for num in arr:
        if num > 2048:
            continue
        freq[num] = freq.get(num, 0) + 1

    power = 1
    while power < 2048:
        count = freq.get(power, 0)
        freq[power * 2] = freq.get(power * 2, 0) + count // 2
        power *= 2

    if freq.get(2048, 0) >= 1:
        print("YES")
    else:
        print("NO")
#字典的运用，用get()合成大西瓜



