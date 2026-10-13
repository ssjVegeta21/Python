
""" ================================== LeetCode Version ======================================

- Time Complexity: O(k) #Where k is the number of bits in the binary representation of n
- Space Complexity: O(1) 

class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0

        while n:
            count += n & 1
            n >>= 1

        return count
========================================================================================== """

# ================================== Runnable Version ========================================

class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0

        while n:
            count += n & 1
            n >>= 1

        return count

sol = Solution()
n = int(input("Enter a number : "))

print(f"Number of 1 bits in the binary representation of {n} is : {sol.hammingWeight(n)}")