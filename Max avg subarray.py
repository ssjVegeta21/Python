
""" ================================== LeetCode Version ======================================

- Time Complexity: O(n) 
- Space Complexity: O(1) 

class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        n = len(nums)
        Sum = 0
        maxSum = 0

        for i in range(k):
            Sum += nums[i]
        maxSum = Sum

        for i in range(k,n):
            Sum -= nums[i - k]
            Sum += nums[i]
            if Sum > maxSum: maxSum = Sum

        return maxSum / k
========================================================================================== """

# ================================== Runnable Version ========================================

class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        n = len(nums)
        Sum = 0
        maxSum = 0

        for i in range(k):
            Sum += nums[i]
        maxSum = Sum

        for i in range(k,n):
            Sum -= nums[i - k]
            Sum += nums[i]
            if Sum > maxSum: maxSum = Sum

        return maxSum / k

sol = Solution()
n = int(input("Enter the number of elements in the array : "))
nums = []

print("Enter the elements of the array : ", end="")
for i in range(n):
    nums.append(int(input()))

k = int(input("Enter the value of k : "))
result = sol.findMaxAverage(nums, k)

print(f"The maximum average of any subarray of length {k} is: {result}")    