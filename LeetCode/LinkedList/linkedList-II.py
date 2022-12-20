# Definition for singly-linked list.
class Node:
    next = None

    def __init__(self, val) -> None:
        self.val = val

    def __repr__(self) -> str:
        return(f'{self.val} -> {self.next}')


# Time Complexity - O(N)
#Space Complexity - O(1)
# class Solution:
#     def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         slow = head
#         fast = head
#         flag = 0
  

#         while fast and fast.next:
#             slow = slow.next
#             fast = fast.next.next

#             if slow == fast:
#                 flag = 1
#                 break

#         if flag == 0:
#             return None

#         else:
#             slow = head
#             while slow != fast:
#                 slow = slow.next
#                 fast = fast.next

#             return slow

# Time Complexity - O(N)
# Space Complexity - O(n)
class SolutionOne(object):
    def detectCycle( head):
        # Key = id
        # Value = Node
        ids = dict()
        while(head != None):
            instanceid = id(head)
            if instanceid in ids:
                return ids[instanceid]
            else:
                ids[instanceid] = head
            head = head.next
        return None


head = Node(3)
head.next = Node(2)
head.next.next = Node(0)
head.next.next.next = Node(-4)
head.next.next.next.next = head.next
print(SolutionOne.detectCycle(head))
