class Solution(object):
    def findMatrix(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        output = []
        count = {}
        for val in nums:
            if val not in count:
                if len(output) == 0:
                    output.append([])
                output[0].append(val)
                count[val] = 1
            else:
                count[val] += 1
                if count[val] > len(output):
                    output.append([])
                output[count[val]-1].append(val)
                
        return output

    def second_ans(self,nums):
        unique_nums = set(nums)
        for val in unique_nums:
            num_count = nums.count(val)
            for idx in range(num_count):
                if len(output) > idx:
                    output[idx].append(val)
                else:
                    output.append([val])

        return output
