# -*- coding:utf-8 -*-
# 给定一个二叉树，找出其最大深度。

# 二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。

# 说明: 叶子节点是指没有子节点的节点。
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
        	return 0
        leftLen = self.maxDepth(root.left)
        rightLen = self.maxDepth(root.right)

        if leftLen > rightLen:
        	return leftLen + 1
        else:
        	return rightLen + 1

        