# -*- coding:utf-8 -*-
# 给定一个二叉树，检查它是否是镜像对称的。

# 例如，二叉树 [1,2,2,3,4,4,3] 是对称的。
# 但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:
# 如果你可以运用递归和迭代两种方法解决这个问题，会很加分。
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def preOrderTraverse(tree,tree_list):
        	if tree == None:
        		tree_list.append('null')
        	else:
        		tree_list.append(tree.val)
        		preOrderTraverse(tree.left,tree_list)
        		preOrderTraverse(tree.right,tree_list)
        	return tree_list

        def preOrderTraverse2(tree,tree_list):
        	if tree == None:
        		tree_list.append('null')
        	else:
        		tree_list.append(tree.val)
        		preOrderTraverse2(tree.right,tree_list)
        		preOrderTraverse2(tree.left,tree_list)
        	return tree_list

        p1 = preOrderTraverse(root,[])
        p2 = preOrderTraverse2(root,[])

        if p1 == p2:
        	return True
        else:
        	return False