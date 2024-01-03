class Solution(object):
    def numberOfBeams(self, bank):
        """
        :type bank: List[str]
        :rtype: int
        """
        output = 0
        start = 0
        for row in bank:
            ones = row.count('1')
            if ones != 0:
                output += start*ones
                start = ones
        return output
