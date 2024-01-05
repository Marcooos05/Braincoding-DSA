class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        temp = [nums[0]]
        length = 1

        for i in range(1, len(nums)):
            if temp[-1] < nums[i]:
                temp.append(nums[i])
                length += 1
            else:
                ind = bisect.bisect_left(temp, nums[i])
                temp[ind] = nums[i]

        return length
        
