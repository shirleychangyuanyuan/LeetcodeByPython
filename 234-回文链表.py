# -*- coding:utf-8 -*-
# 请判断一个链表是否为回文链表。
# 进阶：
# 你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
	def reverse(self,head):
		if head == None:
			return []
		list = []
		while head:
			list.insert(0,head.val)
			head = head.next
		return list
	def forward(self,head):
		if head == None:
			return []
		list = []
		while head:
			list.append(head.val)
			head = head.next
		return list
	def isPalindrome(self, head):
		forward_list = self.forward(head)
		reverse_list = self.reverse(head)
		return forward_list == reverse_list

if __name__ == '__main__':
	node1 = ListNode(1)
	node2 = ListNode(2)
	node3 = ListNode(2)
	node4 = ListNode(1)
	node1.next = node2
	node2.next = node3
	node3.next = node4
	print(Solution().isPalindrome(node1))