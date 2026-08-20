class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dictionary = {}
        for i in nums:
            if i not in dictionary:
                dictionary[i] = 1
            else:
                return True
        return False
        
