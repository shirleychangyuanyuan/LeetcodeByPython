# -*- coding:utf-8 -*-
# 给定一个二叉搜索树, 找到该树中两个指定节点的最近公共祖先。

# 百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，
# 最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”

# 所有节点的值都是唯一的。
# p、q 为不同节点且均存在于给定的二叉搜索树中。

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        pointer = root
        while pointer:
        	if p.val < pointer.val and q.val < pointer.val:
        		pointer = pointer.left
        	elif p.val > pointer.val and q.val > pointer.val:
        		pointer = pointer.right
        	else:
        		return pointer