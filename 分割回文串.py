class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_huiwen(string):
            return string==string[::-1]
        def dfs(path,start):
            if start==len(s):
                result.append(path[:])
                return
            for end in range(start+1,len(s)+1):
                string=s[start:end]
                if is_huiwen(string):
                    path.append(string)
                    dfs(path,end)
                    path.pop()
        result=[]
        dfs([],0)
        return result
