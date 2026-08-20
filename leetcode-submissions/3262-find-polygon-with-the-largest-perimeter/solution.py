class Solution(object):
    def largestPerimeter(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        output = []

        for i in range(len(nums)-1, 1, -1):
            if sum(nums[:i])> nums[i]:
                output = nums[:i+1]
                break
        if len(output) >= 3:
            return sum(output)
        else:
            return -1
