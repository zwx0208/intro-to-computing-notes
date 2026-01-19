class Solution:
    def maxSum(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums, reverse=True)
        num_list = []
        for n in sorted_nums:
            if sorted_nums[0]>0:
                if n not in num_list and n > 0:
                    num_list.append(n)
            else:
                num_list.append(sorted_nums[0])
                break
        return sum(num_list)
#用排序时间复杂度会比较大

class Solution:
    def maxSum(self, nums: List[int]) -> int:
        s = set()
        ans = 0
        mi = -inf
        for num in nums:
            if num > 0 and num not in s:
                s.add(num)
                ans += num
            mi = max(mi,num)
        return ans if len(s) != 0 else mi
