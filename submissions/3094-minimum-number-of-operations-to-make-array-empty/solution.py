class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min_move = 0
        val_dict = {}
        for val in nums:
            if val in val_dict:
                val_dict[val] += 1
            else:
                val_dict[val] = 1
        
        for count in val_dict.values():
            if count == 1:
                return -1
            else:
                if count % 3 != 0:
                    min_move += 1
                    min_move += count//3
                else:
                    min_move += count/3
        return min_move
