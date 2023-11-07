class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = ""
        max_len = 0
        #for i in range(len(s)):
        for char in s:
            if char not in result:
                result += char
                continue
            if len(result) > max_len:
                max_len = len(result)
            repeatidx = result.index(char)
            result = result[repeatidx+1:]+char
    #checking for cases in which the longest string is up to the last character
        if len(result) > max_len:
            max_len = len(result)
        result = ""
        return max_len

