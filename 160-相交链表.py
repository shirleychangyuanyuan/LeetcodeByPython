# -*- coding:utf-8 -*-

# 编写一个程序，找到两个单链表相交的起始节点。

# 注意：

# 如果两个链表没有交点，返回 null.
# 在返回结果后，两个链表仍须保持原有的结构。
# 可假定整个链表结构中没有循环。
# 程序尽量满足 O(n) 时间复杂度，且仅用 O(1) 内存。
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA == None or headB == None:
        	return None

        def readLen(head):
        	count = 0
        	while(head):
        		head = head.next
        		count += 1
        	return count
        lenA = readLen(headA)
        lenB = readLen(headB)

        if lenA >= lenB:
        	for i in range(lenA - lenB):
        		headA = headA.next
        else:
        	for i in range(lenB - lenA):
        		headB = headB.next

        while headA and headB and headA != headB:
        	headA = headA.next
        	headB = headB.next
        return headA
