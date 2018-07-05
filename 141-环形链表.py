# -*- coding:utf-8 -*-
# 给定一个链表，判断链表中是否有环。

# 进阶：
# 你能否不使用额外空间解决此题？
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        fast = slow = head
        while fast and fast.next:
        	fast = fast.next.next
        	slow = slow.next
        	if fast == slow:
        		return True

        return False