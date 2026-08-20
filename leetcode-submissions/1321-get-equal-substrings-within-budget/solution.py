class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        totalCost = 0
        maxlength = 0
        l = 0

        for i in range(len(s)):
            totalCost += abs(ord(t[i])-ord(s[i]))
            while totalCost > maxCost:
                totalCost -= abs(ord(t[l])-ord(s[l]))
                l += 1
            maxlength = max(maxlength, i-l+1)

        return maxlength
