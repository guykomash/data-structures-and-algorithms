
'''
206. Reverse Linked List
https://leetcode.com/problems/reverse-linked-list/description/
'''

class LinkNode:
    def __init__(self,val, next=None):
        self.val = val
        self.next = next


def reverseLinkedList(head):
    if not head: return
    prev = None
    cur = head
    while cur:
        tmp = cur.next
        cur.next = prev
        prev = cur
        cur = tmp
    return prev