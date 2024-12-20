# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head):
        # 和归并排序数组一样，链表也要先找到中点，然后断开，最后合并

        if not head or not head.next:
            return head
        # 使用快慢指针的方式找中点
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # 从slow后面断开
        mid = slow.next
        slow.next = None

        # 递归断开
        left = self.sortList(head)
        right = self.sortList(mid)

        dumb = ListNode(0)
        cur = dumb
        while left and right:
            if left.val <= right.val:
                cur.next = left
                left = left.next
            else:
                cur.next = right
                right = right.next
            cur = cur.next
        if left:
            cur.next = left
        else:
            cur.next = right
        return dumb.next


if __name__ == '__main__':
    # ls = [3, 2, 4, 6, 5, 1, 7, 8]
    n3 = ListNode(3, ListNode(2, ListNode(4, ListNode(6, ListNode(5, ListNode(1, ListNode(7, ListNode(8))))))))
    # n2 = ListNode(2)
    # n4 = ListNode(4)
    # n6 = ListNode(6)
    # n5 = ListNode(5)
    # n1 = ListNode(1)
    # n7 = ListNode(7)
    # n8 = ListNode(8)
    s = Solution()
    ret = s.sortList(n3)
    cur = ret
    while cur:
        print(cur.val, end='')
        cur = cur.next
