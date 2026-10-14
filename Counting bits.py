
""" ================================== LeetCode Version ======================================

- Time Complexity: O(n) 
- Space Complexity: O(1) 

class Solution:
    def countBits(self, n: int) -> list[int]:
        ans = (n + 1) * [0]

        for i in range(1, n+1):
            ans[i] = ans[i >> 1] + (i & 1)
            # i >> 1 is equivalent to integer division by 2
            # Bitwise AND with 1 checks the last bit

        return ans
========================================================================================== """

# ================================== Runnable Version ========================================

class Solution:
    def countBits(self, n: int) -> list[int]:
        ans = (n + 1) * [0]

        for i in range(1, n+1):
            ans[i] = ans[i >> 1] + (i & 1)
            # i >> 1 is equivalent to integer division by 2
            # Bitwise AND with 1 checks the last bit

        return ans

sol = Solution()
n = int(input("Enter a non-negative integer : "))

print(f"Number of 1's in binary representation from 0 to {n} is : {sol.countBits(n)}")