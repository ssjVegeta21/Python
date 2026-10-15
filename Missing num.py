
""" ================================== LeetCode Version ======================================

- Time Complexity: O(n) 
- Space Complexity: O(1) 

class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        Sum = 0
        expected_sum = n*(n + 1) // 2

        for i in range(n):
            Sum += nums[i]

        miss_num = expected_sum - Sum
        return miss_num
========================================================================================== """

# ================================== Runnable Version ========================================

class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        Sum = 0
        expected_sum = n*(n + 1) // 2

        for i in range(n):
            Sum += nums[i]

        miss_num = expected_sum - Sum
        return miss_num

sol = Solution()
n = int(input("Enter the length of the array : "))
nums = list(map(int, input("Enter the elements of the array separated by spaces: ").split()))

print("The missing number is :", sol.missingNumber(nums))