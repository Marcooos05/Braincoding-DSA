class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        rob = 0
        norob = 0

        for val in nums:
            newRob = norob + val
            norob = max(rob, norob)
            rob = newRob

        return max(rob, norob)
