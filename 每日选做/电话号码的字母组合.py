def phonenumbers(digits):
    result=[]
    num_dict={'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'qrs','8':'tuv','9':'wxyz'}
    def backtrack(index,path):
        #index: 当前处理的数字在digits中的索引
        #path: 当前构建的字母组合
        if index==len(digits):
            result.append(path)
            return
        d=digits[index]   #d是当前数字
        letters=num_dict[d]
        for l in letters:
            backtrack(index+1,path+l)  #将当前字母添加，处理下一个数字
    backtrack(0,'')
    return result






