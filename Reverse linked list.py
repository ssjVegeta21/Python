
""" ================================== LeetCode Version ======================================

- Time Complexity: O(n) 
- Space Complexity: O(1) 

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        if head == None: return head

        prev = None
        curr = head
        nxt = None

        while curr != None:
            nxt = curr.next   # Save the next node
            curr.next = prev   # Reverse the pointer
            prev = curr    # Move prev forward
            curr = nxt    # Move curr forward
        
        return prev
========================================================================================== """

# ================================== Runnable Version ========================================

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        if head == None: return head

        prev = None
        curr = head
        nxt = None

        while curr != None:
            nxt = curr.next   # Save the next node
            curr.next = prev   # Reverse the pointer
            prev = curr    # Move prev forward
            curr = nxt    # Move curr forward
        
        return prev

sol = Solution()
n = int(input("Enter the number of nodes in the linked list : "))
head = None

for i in range(n):
    val = int(input(f"Enter the value of node {i+1} : "))
    new_node = ListNode(val)

    if head is None:
        head = new_node
        tail = new_node
    else:
        tail.next = new_node
        tail = new_node

rev_head = sol.reverseList(head)

print("Reversed linked list : ", end="")
while rev_head is not None:
    print(rev_head.val, end="->")
    rev_head = rev_head.next
    
if rev_head is None: print("None")  