def max_matrix(matrix):
    def kadane(l):
        max_current=max_global=l[0]
        for x in l[1:]:
            max_current= max(x, max_current + x)
            max_global= max(max_current, max_global)
        return max_global
    rows = len(matrix)
    cols = len(matrix[0])
    max_sum = float('-inf')
    for left in range(cols):
        temp = [0] * rows
        for right in range(left, cols):
            for row in range(rows):
                temp[row] += matrix[row][right]
            max_sum = max(max_sum, kadane(temp))
    return max_sum
n = int(input())
nums = []
while len(nums)<n**2:
    nums.extend(input().split())
matrix = [list(map(int,nums[i*n:(i+1)*n])) for i in range(n)]
max_sum = max_matrix(matrix)
print(max_sum)