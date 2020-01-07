#1. 合并两个有序链表
"""
将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。
输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4

"""
# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 == None and l2 == None:
            return None
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        p1 = l1
        p2 = l2
        p = ListNode(-1)
        res = p
        while p1 and p2:
            if p1.val > p2.val:
                p.next = p2
                p = p.next
                p2 = p2.next
            else:
                p.next = p1
                p = p.next
                p1 = p1.next
        if p1:
            p.next = p1
        else:
            p.next = p2
        return res.next

#2. 删除链表的倒数第N个节点
"""
给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。

给定一个链表: 1->2->3->4->5, 和 n = 2.
当删除了倒数第二个节点后，链表变为 1->2->3->5.

给定的 n 保证是有效的。
进阶：
你能尝试使用一趟扫描实现吗
"""


def removeNthFromEnd(self, head, n):
    """
    :type head: ListNode
    :type n: int
    :rtype: ListNode
    """
    if head == None:
        return None
    f = head
    s = head
    res = s
    while n > 0:
        f = f.next
        n -= 1
    if f == None:
        return res.next
    while s:
        if f.next == None:
            s.next = s.next.next
            s = s.next
            return res
        else:
            f = f.next
            s = s.next

#3. 旋转链表
"""
给定一个链表，旋转链表，将链表每个节点向右移动k个位置，其中k是非负数。
示例 1:
输入: 1->2->3->4->5->NULL, k = 2
输出: 4->5->1->2->3->NULL

解释:
向右旋转 1 步: 5->1->2->3->4->NULL
向右旋转 2 步: 4->5->1->2->3->NULL

示例 2:
输入: 0->1->2->NULL, k = 4
输出: 2->0->1->NULL

解释:
向右旋转 1 步: 2->0->1->NULL
向右旋转 2 步: 1->2->0->NULL
向右旋转 3 步: 0->1->2->NULL
向右旋转 4 步: 2->0->1->NULL
"""


def rotateRight(self, head, k):
    """
    :type head: ListNode
    :type k: int
    :rtype: ListNode
    """
    if head == None:
        return None
    b = head
    p = head
    n = 1
    while p.next:
        n += 1
        p = p.next
    p.next = b
    if k <= n:
        a = n - k
        while a > 0:
            p = p.next
            a -= 1
        newb = p.next
        p.next = None
        return newb
    else:
        a = n - k % n
        while a > 0:
            p = p.next
            a -= 1
        newb = p.next
        p.next = None
        return newb