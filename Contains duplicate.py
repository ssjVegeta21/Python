
""" ================================== LeetCode Version ======================================

- Time Complexity: O(n) 
- Space Complexity: O(1) 

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        already_seen = set()

        for num in nums:
            if num in already_seen:
                return True                
            already_seen.add(num)

        return False
========================================================================================== """

# ================================== Runnable Version ========================================

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        already_seen = set()

        for num in nums:
            if num in already_seen:
                return True                
            already_seen.add(num)

        return False

sol = Solution()
n = int(input("Enter the number of elements in the list :  "))
nums = list(map(int, input("Enter the elements of the list separated by spaces : ").split()))

print("\nDoes the list contain duplicates? : ", end ="")
if sol.containsDuplicate(nums): print("Yes")
else: print("No")