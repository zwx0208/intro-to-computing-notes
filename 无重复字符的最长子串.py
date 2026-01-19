class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n=len(s)
        l,r,count=0,0,0
        char_set = set()
        while r < n:
            if s[r] not in char_set:
                char_set.add(s[r])
                r += 1
                count = max(count, r - l)
            else:
                char_set.remove(s[l])
                l += 1
        return count
#力扣不是print是return