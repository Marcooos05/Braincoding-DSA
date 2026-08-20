class Solution:
    #key point: if k is less than the length of the list nums, only the first and last indexed Integer will appear in at most one subarray. We must also check that the Integers are not duplicated in the list

    #Review: 
    #1. Even though the constraints is set such that checking through all the possible values 1-50 is O(1) time complexity, since the length of the list will be no longer than 50, O(n) in this scenario is actually faster than supposed O(1) (actual O(50)) since n will be less than or equal to 50. Had the length of list nums be infinite, iterating through the constraints should allow for a more optimised time complexity
    #2. A Hashmap to act as a counter is very memory intensive, for this question where the numbers are sequentially spaced a list would be a better use of memory than a dictionary. That said, using set to track unique values was about the same memory usage, and I personally preferred the set difference notation given it is quite an overlooked and useful function.
    #3. Pattern recognition was required for k != 1 and k != nums.length. It was fun to identify that interesting pattern that only the first and last indexed value will not be repeated in more than one subarray. Beyond that where k = nums.length, using a max function would suffice. And surprisingly the case where one could consider optimisation is when k == 1 whereby we need to find the highest unique value in the list, where set difference was something I found very useful.
    #4. One beginner-friendly solution would be an O(n^2) solution that iterates through the list and does a separate count function which would be O(n) as well, however it can be noted that it is possible to simplify it into an O(n) solution

    def largestInteger(self, nums: List[int], k: int) -> int:
        if k == len(nums):
            return max(nums)
        elif k == 1:
            #Attempting a space optimised solution, using array instead of set
            count = [0] *51
            for i in nums:
                count[i] += 1
            for index in range(len(count)-1,-1,-1):
                if count[index] == 1:
                    return index
            return -1
            #Conclusion: memory usage is similar between set and array in this question

            #return the max unique value using set to easily do set difference
            dups = set()
            seen = set()
            for i in nums:
                if i in seen:
                    dups.add(i)
                else:
                    seen.add(i)
            unique = list(seen - dups)
            if unique != []:
                return max(unique)
            else:
                return -1
            
        else:
            start_check = nums[0] not in nums[1:]
            end_check = nums[-1] not in nums[:-1]

            #checking if start and end index are unique
            if start_check and end_check: 
                return max(nums[0], nums[-1])
            elif start_check:
                return nums[0]
            elif end_check:
                return nums[-1]
            else:
                return -1

        
    def largestInteger_first(self, nums: List[int], k: int) -> int:
        #using hash to store count
        hashCount = {i:0 for i in range(0,51)}

        #O(1) time complexity since we iterate through a fixed length, only possible due to the constraints set
        for val in hashCount.keys(): 
            hashCount[val] = nums.count(val)

        uniqueVal = [-1]
        for key, val in hashCount.items():
            if val == 1:
                uniqueVal.append(key)
        #shortened for loop
        #uniqueVal = [key for key, val in hashCount.items() if val == 1]

        #every index will only appear in one subarray
        if k == 1:
            #return the max value with count of 1
            return max(uniqueVal)

        #key section, unique to question
        elif k < len(nums):
            #return the highest unqiue val between the first and last indexed value
            if nums[0] in uniqueVal and nums[-1] in uniqueVal:
                return max(nums[0], nums[-1])
            elif nums[0] in uniqueVal:
                return nums[0]
            elif nums[-1] in uniqueVal:
                return nums[-1]
            else:
                return -1
        
        #since all index exist in one subarray, return the max of all the values
        elif k == len(nums):
            return max(nums)

        return -1
