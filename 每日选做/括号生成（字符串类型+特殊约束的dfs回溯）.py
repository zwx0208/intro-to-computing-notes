"""
约束条件：
left ≤ n（不能超过n个左括号）
right ≤ left（右括号不能多于左括号，否则无效）

    left: 已使用的左括号数量
    right: 已使用的右括号数量
    path: 当前构建的括号字符串
"""
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result=[]
        def dfs(l,r,path):
            if len(path)==n*2:
                result.append(path)
                return
            if l<n:
                dfs(l+1,r,path+'(')
            if r<l:
                dfs(l,r+1,path+')')
        dfs(0,0,'')
        return result


'''字符串是不可变类型：path + '(' 没有修改原字符串，而是创建了一个新字符串！'''
