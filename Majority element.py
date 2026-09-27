
""" ================================== LeetCode Version ======================================

- Time Complexity: O(n) 
- Space Complexity: O(1) 

class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        n = len(nums)
        candidate = 0
        count = 0

        # Here, we use the Boyer-Moore voting algorithm.
        # This loop finds a potential majority element by balancing the opposing elements.
        for num in nums:
            # If the current vote hits zero, pick a new candidate.
            if count == 0:
                candidate = num

            # If the current number matches the candidate, increment the count. Otherwise, decrement it.
            count += 1 if num == candidate else -1


        # Boyer-Moore always finds a candidate. 
        # This loop confirms if it is a true majority.
        freq = 0
        for num in nums:
            # Count the total occurrence of our selected candidate.
            if num == candidate:
                freq += 1

        # Return the candidate if it appears more than half the time, otherwise return -1.
        return candidate if freq > n // 2 else -1 
========================================================================================== """

# ================================== Runnable Version ======================================

class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        n = len(nums)
        candidate = 0
        count = 0

        # Here, we use the Boyer-Moore voting algorithm.
        # This loop finds a potential majority element by balancing the opposing elements.
        for num in nums:
            # If the current vote hits zero, pick a new candidate.
            if count == 0:
                candidate = num

            # If the current number matches the candidate, increment the count. Otherwise, decrement it.
            count += 1 if num == candidate else -1


        # Boyer-Moore always finds a candidate. 
        # This loop confirms if it is a true majority.
        freq = 0
        for num in nums:
            # Count the total occurrence of our selected candidate.
            if num == candidate:
                freq += 1

        # Return the candidate if it appears more than half the time, otherwise return -1.
        return candidate if freq > n // 2 else -1 


n = int(input("Enter the number of elements in the list: "))
nums = []
print("Enter the elements of the list: ")
for i in range(n):
    nums.append(int(input()))

sol = Solution()
result = sol.majorityElement(nums)
if result != -1:
    print("The majority element is:", result)
else:
    print("No element appears more than half the time. Therefore, there is no majority element.")