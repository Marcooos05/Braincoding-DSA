class Solution(object):
    def maxScore(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_sum = 0
        for ind in range(1,len(s)):
            zeros = s[:ind]
            ones = s[ind:]
            total_sum = zeros.count("0") + ones.count("1")
            max_sum = max(max_sum, total_sum)
        return max_sum
