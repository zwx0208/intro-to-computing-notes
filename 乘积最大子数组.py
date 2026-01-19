class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans=nums[0]
        n=len(nums)
        max_dp=[0]*n
        min_dp=[0]*n
        min_dp[0]=max_dp[0]=nums[0]
        for i in range(1,n):
            candidates=[nums[i],nums[i]*max_dp[i-1],nums[i]*min_dp[i-1]]
            max_dp[i]=max(candidates)
            min_dp[i]=min(candidates)
            ans=max(ans,max_dp[i])
        return ans


#思路很清晰：需要维护三个候选，每个点的最大都可能是：当前数字，当前数字乘之前最大，当前数字乘之前最小
#由于候选一定含当前数字，所以一定是连续到当前数字的一个子集

