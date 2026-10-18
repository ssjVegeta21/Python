
""" ================================== LeetCode Version ======================================

- Time Complexity: O(n) 
- Space Complexity: O(1) 

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast: return True

        return False
========================================================================================== """

# ================================== Runnable Version ========================================

from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast: return True

        return False

def helper(values: list[int], pos: int) -> Optional[ListNode]:
    if not values: return None
        
    nodes = [ListNode(val) for val in values]

    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]

    if pos >= 0 and pos < len(nodes):
        nodes[-1].next = nodes[pos]
        
    return nodes[0]

sol = Solution()
raw_vals = input("Enter node values separated by commas : ")
val_list = [int(x.strip()) for x in raw_vals.split(",") if x.strip()]
    
pos_input = input("Enter cycle index position (-1 for no cycle): ")
cycle_pos = int(pos_input.strip())
head_node = helper(val_list, cycle_pos)
    
has_cycle = sol.hasCycle(head_node)
    
print("\nDoes the list have any cycle? : ", end="")
if has_cycle: print("Yes")
else: print("No")
