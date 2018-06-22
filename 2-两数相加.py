# -*- coding:utf-8 -*-
#给定两个非空链表来代表两个非负整数，位数按照 *逆序* 方式存储，它们的每个节点只存储 *单个* 数字。将这两数相加会返回一个新的链表。
#你可以假设除了数字 0 之外，这两个数字都不会以零开头。
# Definition for singly-linked list.
class ListNode:
    def __init__(self,x):
        self.val=x
        self.next=None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry=0
        res=n=ListNode(0)
        while l1 or l2 or carry:
            if l1:
                carry+=l1.val
                l1=l1.next
            if l2:
                carry+=l2.val
                l2=l2.next
            carry,val=divmod(carry,10)#返回商，余数
            n.next=n=ListNode(val)
        return res.next