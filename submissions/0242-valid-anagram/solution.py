class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        sDict = {}
        tDict = {}

        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            if s[i] not in sDict:
                sDict[s[i]] = 1
            else:
                sDict[s[i]] += 1
            if t[i] not in tDict:
                tDict[t[i]] = 1
            else:
                tDict[t[i]] += 1
        if tDict == sDict:
            return True
        else:
            return False

        
