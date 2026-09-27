
""" ================================== LeetCode Version ======================================

- Time Complexity: O(n) 
- Space Complexity: O(1) 

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # Create an empty dictionary to keep track of the numbers seen so far  {number : index}
        dicti = {}
        n = len(nums)

        for i in range(n):
            # Calculate the value needed to reach the target
            val = target - nums[i] 

            # If the value is already seen, return the index of the previously seen number and current index
            if val in dicti:
                return [dicti[val], i]

            # Store current number and its index in the dictionary for further calculations  
            dicti[nums[i]] = i

        # Return an empty list if no pair matches the target      
        return []
========================================================================================== """

# ================================== Runnable Version ======================================

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # Create an empty dictionary to keep track of the numbers seen so far  {number : index}
        dicti = {}
        n = len(nums)

        for i in range(n):
            # Calculate the value needed to reach the target
            val = target - nums[i] 

            # If the value is already seen, return the index of the previously seen number and current index
            if val in dicti:
                return [dicti[val], i]

            # Store current number and its index in the dictionary for further calculations  
            dicti[nums[i]] = i

        # Return an empty list if no pair matches the target      
        return []


nums = list(map(int, input("Enter numbers separated by spaces : ").split()))
target = int(input("Enter target : "))

sol = Solution()
result = sol.twoSum(nums, target)

print("Indices :", result)