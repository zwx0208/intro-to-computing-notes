n = int(input())
words = input().split()
line = []
current_length = 0
for word in words:
    if not line:
        line.append(word)
        current_length = len(word)
    else:
        if current_length + 1 + len(word) <= 80:
            line.append(word)
            current_length += 1 + len(word)
        else:
            print(" ".join(line))
            line = [word]
            current_length = len(word)
if line:
    print(" ".join(line))

