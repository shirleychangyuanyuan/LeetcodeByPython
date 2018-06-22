# -*- coding:utf-8 -*-

# 给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
        	return head
        p = head
        while p:
        	while p.next and p.val == p.next.val:
        		p.next = p.next.next
        	p = p.next
        return head
if __name__ == '__main__':
	s1 = ListNode(10)
	s2 = ListNode(12)
	s3 = ListNode(12)
	s1.next = s2
	s2.next = s3
	print(Solution().deleteDuplicates(s1).val)