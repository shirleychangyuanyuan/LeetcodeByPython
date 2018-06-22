# -*- coding:utf-8 -*-
#将两个有序链表合并为一个新的有序链表并返回。
#新链表是通过拼接给定的两个链表的所有节点组成的。 
#Definition for singly-linked list.
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
        if not l1:#注意是看头结点是否为空
        	return l2
        elif not l2:
        	return l1
        if l1.val < l2.val:
        	MergeHead = l1
        	MergeHead.next = self.mergeTwoLists(l1.next,l2)
        else:
        	MergeHead = l2
        	MergeHead.next = self.mergeTwoLists(l1,l2.next)
        return MergeHead
if __name__ == '__main__':
 	node1 = ListNode(1)
 	node2 = ListNode(2)
 	node3 = ListNode(4)
 	node1.next = node2
 	node2.next = node3

 	node4 = ListNode(1)
 	node5 = ListNode(3)
 	node6 = ListNode(4)
 	node4.next = node5
 	node5.next = node6
 	print(Solution().mergeTwoLists(node1,node4).val)