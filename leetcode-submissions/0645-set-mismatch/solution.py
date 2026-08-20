class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        summation = (len(nums)+1) * len(nums)/2
        repeat = sum(nums) - sum(set(nums))
        missing = summation - sum(set(nums))

        return[repeat, missing]
            
