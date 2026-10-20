
""" ================================== LeetCode Version ======================================

- Time Complexity: O(n) where n is the length of the strings s and t 
- Space Complexity: O(1) 

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        freq = 26 * [0]

        for i in range(len(s)):
            freq[ord(s[i]) - ord('a')] += 1
            freq[ord(t[i]) - ord('a')] -= 1

        for count in freq:
            if count != 0: return False

        return True
========================================================================================== """

# ================================== Runnable Version ========================================

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        freq = 26 * [0]

        for i in range(len(s)):
            freq[ord(s[i]) - ord('a')] += 1
            freq[ord(t[i]) - ord('a')] -= 1

        for count in freq:
            if count != 0: return False

        return True

sol = Solution()
first_string = input("Enter the first string (s): ").strip()
second_string = input("Enter the second string (t): ").strip()
    
result = sol.isAnagram(first_string, second_string)

print("\nResult : ", end="")
if result:
    print(f"Success! '{first_string}' and '{second_string}' ARE anagrams of each other.")
else:
    print(f"'{first_string}' and '{second_string}' ARE NOT anagrams.")