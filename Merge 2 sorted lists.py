
""" ================================== LeetCode Version ======================================

- Time Complexity: O(n + m) # Where n and m are the lengths of the two linked lists
- Space Complexity: O(1) 

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        mergedList = ListNode(0)
        curr = mergedList

        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            
            else:
                curr.next = list2
                list2 = list2.next
            
            curr = curr.next
        
        if list1: curr.next = list1
        else: curr.next = list2

        return mergedList.next
========================================================================================== """

# ================================== Runnable Version ========================================

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        mergedList = ListNode(0)
        curr = mergedList

        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            
            else:
                curr.next = list2
                list2 = list2.next
            
            curr = curr.next
        
        if list1: curr.next = list1
        else: curr.next = list2

        return mergedList.next

sol = Solution()
n = int(input("Enter the number of nodes in the linked list 1 : "))
list1 = None
for i in range(n):
    val = int(input("Enter the value for node : "))
    if not list1:
        list1 = ListNode(val)
        curr = list1
    else:
        curr.next = ListNode(val)
        curr = curr.next

m = int(input("Enter the number of nodes in the linked list 2 : "))
list2 = None
for i in range(m):
    val = int(input("Enter the value for node : "))
    if not list2:
        list2 = ListNode(val)
        curr = list2
    else:
        curr.next = ListNode(val)
        curr = curr.next

merged = sol.mergeTwoLists(list1, list2)

curr = merged
values = []
while curr:
    values.append(curr.val)
    curr = curr.next

print("\nMerged linked list : ", values)
