class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        
        for first_idx in range(len(nums)):
            result = [first_idx]
            value = target - nums[first_idx]
            sublst = nums[first_idx+1:]

            if value in sublst:
                sec_idx = sublst.index(value)
                result.append(sec_idx+first_idx+1)
                return result
