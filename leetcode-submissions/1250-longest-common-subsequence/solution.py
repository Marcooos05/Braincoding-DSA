class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        #initialise a 2D array of 0 to contain the length of the longest substring
        dp = [[0 for _ in range(len(text1) + 1)] for _ in range(len(text2) + 1)]

        for idx1 in range(len(text2) - 1, -1, -1):
            for idx2 in range(len(text1) - 1, -1, -1):
                if text2[idx1] == text1[idx2]:
                    dp[idx1][idx2] = 1 + dp[idx1+1][idx2+1]
                else:
                    dp[idx1][idx2] = max(dp[idx1 + 1][idx2], dp[idx1][idx2 + 1])

        return dp[0][0]
