n=int(input())
bricks=[]
words=[]
for _ in range(4):
    bricks.append(input())
def can_spell(word, bricks):
    l = len(word)
    used = [False] * 4
    def backtrack(pos):
        if pos == l:
            return True
        for i in range(4):
            if not used[i] and word[pos] in bricks[i]:
                used[i] = True
                if backtrack(pos + 1):
                    return True
                used[i] = False
        return False
    return backtrack(0)

for _ in range(n):
    v=input()
    print('YES' if can_spell(v,bricks) else "NO")