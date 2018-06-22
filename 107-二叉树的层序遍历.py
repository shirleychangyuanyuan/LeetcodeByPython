# -*- coding:utf-8 -*-
# 给定一个二叉树，返回其节点值自底向上的层次遍历。 （即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
        	return []

        current = [root]
        result = []

        while current:
        	next_level,vals = [],[]
        	for node in current:
        		vals.append(node.val)
        		if node.left:
        			next_level.append(node.left)#注意这边添加的左节点，而不是左节点的值
        		if node.right:
        			next_level.append(node.right)
        	current = next_level
        	result.append(vals)

        return result[::-1]