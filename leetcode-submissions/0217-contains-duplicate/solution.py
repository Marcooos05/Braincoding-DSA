class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)

    def containsDuplicate_hashAttempt(self, nums: List[int]) -> bool:
        #using hash to possibly improve memory usage
        hashCount = {}
        for num in nums:
            if num not in hashCount:
                hashCount[num] = 1
            else:
                return True
        return False
    
    def containsDuplicate_setAttempt(self, nums: List[int]) -> bool:
        #set difference method, good runtime, memory not optimal
        #dup = set() - initally used a duplicate set to track duplicates but not actually needed, it can be simplified to return immediately on detecting a duplicate
        seen = set()
        for num in nums:
            if num not in seen:
                seen.add(num)
            else:
                return True
        return False
