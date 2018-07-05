# -*- coding:utf-8 -*-
# 给定一个二叉树，返回所有从根节点到叶子节点的路径。

# 说明: 叶子节点是指没有子节点的节点。
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
    	res, path_list = [], []
    	self.dfs(root, path_list, res)
    	return res
    	
    def dfs(self, root, path_list, res):
    	if not root:
    		return 
    	path_list.append(str(root.val))
    	#如果到了叶子节点
    	if not root.left and not root.right:
    		res.append('->'.join(path_list))
    	if root.left:
    		self.dfs(root.left, path_list, res)
    	if root.right:
    		self.dfs(root.right, path_list, res)
    	path_list.pop()


if __name__ == '__main__':
	node1 = TreeNode(1)
	node2 = TreeNode(2)
	node3 = TreeNode(5)
	node4 = TreeNode(3)
	node1.left = node2
	node1.right = node4
	node2.right = node3
	print(Solution().binaryTreePaths(node1))