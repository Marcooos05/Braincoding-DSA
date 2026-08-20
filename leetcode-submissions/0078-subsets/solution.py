import copy
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = []
        def dp(subset, n):
            if n >= len(nums):
                output.append(subset)
            else:
                new_subset = copy.deepcopy(subset)
                new_subset.append(nums[n])
                dp(subset, n+1)
                dp(new_subset, n+1)
        dp([],0)
        return output
