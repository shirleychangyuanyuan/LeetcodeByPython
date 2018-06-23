# -*- coding:utf-8 -*-
# 给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。
# 在杨辉三角中，每个数是它左上方和右上方的数的和。
# 



# list = [[] for i in range(5)]
# list[3] =[1]
# print(list)
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
        	return []
        if numRows == 1:
        	return [[1]]
        if numRows == 2:
        	return [[1],[1,1]]
        if numRows >2:
        	list = [[] for i in range(numRows)]
        	for i in range(numRows):
        		list[i] = [1 for j in range(i+1)]#[[1], [1, 1], [1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1, 1]]
        	for i in range(2,numRows):
        		for j in range(1,i):
        			list[i][j] = list[i-1][j-1] + list[i-1][j]
        	return list
if __name__ == '__main__':
	print(Solution().generate(5))









