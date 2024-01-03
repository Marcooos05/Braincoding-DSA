class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort() # sort the greeds
        s.sort(reverse = True) # sort the cookies in reverse

        output = 0
        if min(len(g), len(s)) == 0:
            return output
    
        else:
            for idx in range(len(g)):
                while len(s) > 0 and g[idx] > s[-1] :
                    s.pop() # remove cookies that are not able to satisfy the smallest greed

                if len(s) != 0:
                    s.pop() # remove cookie that satisfied the smallest greed
                    output += 1 
        return output 
                
