# -*- coding:utf-8 -*-
# 给定一个二叉树和一个目标和，判断该树中是否存在根节点到叶子节点的路径，这条路径上所有节点值相加等于目标和。

# 说明: 叶子节点是指没有子节点的节点。
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root == None:
        	return False
        if root.left == None and root.right == None:
        	return root.val == sum
        else:
        	return self.hasPathSum(root.left,sum-root.val) or self.hasPathSum(root.right,sum-root.val)