# -*- coding:utf-8 -*-
# 反转一个单链表。
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # new_head = None
        # while head:
        # 	p = head
        # 	head = head.next
        # 	p.next = new_head
        # 	new_head = p
        # return new_head
        new_head = None
        while head:
        	cur = head
        	head = head.next
        	cur.next = new_head
        	new_head = cur
        return new_head

        	