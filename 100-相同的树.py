# -*- coding:utf-8 -*-
# 给定两个二叉树，编写一个函数来检验它们是否相同。

# 如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    # def isSameTree(self, p, q):
    #     """
    #     :type p: TreeNode
    #     :type q: TreeNode
    #     :rtype: bool
    #     """
        def preOrderTraverse(self,tree,tree_list):
        	if tree == None:
        		tree_list.append('null')
        	else:
        		tree_list.append(tree.val)
        		self.preOrderTraverse(tree.left,tree_list)
        		self.preOrderTraverse(tree.right,tree_list)
        	return tree_list
        
        # p_list = preOrderTraverse(p,[])
        # q_list = preOrderTraverse(q,[])

        # if p_list == q_list:
        # 	return True
        # else:
        # 	return False

if __name__ == '__main__':
    root = TreeNode(3)
    node1 = TreeNode(5)
    node2 = TreeNode(10)
    node3 = TreeNode(7)
    node4 = TreeNode(6)
    node5 = TreeNode(5)
    root.left = node1
    root.right = node3
    node1.right = node2
    node3.left = node4
    node3.right = node5
    print(Solution().preOrderTraverse(root,[]))
