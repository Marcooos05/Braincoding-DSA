class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        memo = [0]*len(nums)

        def dp(k):
            if k == len(nums):
                return 0
            if memo[k]:
                return memo[k]
            else:
                m = max(nums[k] + dp(k+1), nums[k])
                memo[k] = m
                return m 
        dp(0)
        return max(memo)
