class Solution:
    def specialArray(self, nums: List[int]) -> int:
        right = len(nums)
        left = 0

        while True:
            n = (left+right)//2
            greater_equal = 0
            for i in nums:
                if i >= n:
                    greater_equal += 1

            if n == greater_equal:
                return n
            if left == right:
                return -1

            if n > greater_equal:
                right = n
            else:
                left = n+1
