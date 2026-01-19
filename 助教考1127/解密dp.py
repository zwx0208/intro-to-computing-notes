def depuzzle(puzzle):
    n = len(puzzle)
    if n <= 1:
        return puzzle
    c = puzzle[0]
    left = puzzle[1:(n+1)//2]
    right = puzzle[(n+1)//2:]
    return depuzzle(left) + [c] + depuzzle(right)
puzzle = list(input().strip())
result = depuzzle(puzzle)
print(''.join(result))  