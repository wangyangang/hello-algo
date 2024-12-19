# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head

        cur = head
        n = 1
        pre = ListNode(0, head)

        while n < left:
            pre = cur
            cur = cur.next
            n += 1

        first = None
        while n <= right:
            if first is not None:
                first = ListNode(cur.val, first)
            else:
                first = ListNode(cur.val)
            n += 1
            cur = cur.next

        pre.next = first

        return head


if __name__ == '__main__':
    ls = [1,2,3,4,5]
    dummy = ListNode(0)
    cur = dummy
    for i in ls:
        cur.next = ListNode(i)
        cur = cur.next

    root = dummy.next
    current = root
    while current:
        print(current.val)
        current = current.next
    print('-------------')

    ret = Solution().reverseBetween(root, 2, 4)
    current = ret
    while current:
        print(current.val)
        current = current.next
