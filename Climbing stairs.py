    
""" ================================== LeetCode Version ======================================

- Time Complexity: O(n) 
- Space Complexity: O(1) 

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2: return n

        ways = [0] * (n + 1)
        ways[1] = 1
        ways[2] = 2

        for i in range(3, n + 1):
            ways[i] = ways[i - 1] + ways[i - 2]

        return ways[n]
========================================================================================== """

# ================================== Runnable Version ========================================

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2: return n

        ways = [0] * (n + 1)
        ways[1] = 1
        ways[2] = 2

        for i in range(3, n + 1):
            ways[i] = ways[i - 1] + ways[i - 2]

        return ways[n]

sol = Solution()
n = int(input("Enter the number of stairs : "))
print(f"Number of ways to climb {n} stairs is : {sol.climbStairs(n)}")
