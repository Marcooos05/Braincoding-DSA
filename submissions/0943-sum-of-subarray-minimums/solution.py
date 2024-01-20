class Solution(object):
    def sumSubarrayMins(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        
        mod = 10**9 + 7
        output = 0
        arr = [float('-inf')] + arr + [float('-inf')] # by sandwiching the arr with values that are infinitely small, all the arrays will be accounted for as they will be poped out by force due to the two infinitely small values
        stack = []

        for idx, num in enumerate(arr):
            while stack and num < stack[-1][1]:
                j, m = stack.pop()
                left = j - stack[-1][0] if stack else j + 1
                right = idx - j
                output = (output + m * (left*right)) % mod

            stack.append((idx,num))

        #stack will be increasing or equal
        #for idx in range(len(stack)):
        #    j, m = stack[idx]
        #    left = j - stack[idx-1][0] if idx > 0 else j + 1
        #    right = len(arr) - j # since all values after it would have been larger due to the nature of the stack
        #    output = output + m * (left*right)

        return output
