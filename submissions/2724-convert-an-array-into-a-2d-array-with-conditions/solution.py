class Solution(object):
    def findMatrix(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        counts = []
        output = []

        unique_nums = set(nums)
        for val in unique_nums:
            num_count = nums.count(val)
            for idx in range(num_count):
                try:
                    output[idx].append(val)
                except:
                    output.append([val])

        return output
