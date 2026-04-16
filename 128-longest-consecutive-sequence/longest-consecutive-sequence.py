class Solution:
    def longestConsecutive(self, nums):
        store = set(nums)
        res = 0

        for num in store:
            if (num - 1) not in store:
                streak = 1
                curr = num
                
                while (curr + 1) in store:
                    curr += 1
                    streak += 1
                
                res = max(res, streak)
                
        return res