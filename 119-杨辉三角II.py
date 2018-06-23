# -*- coding:utf-8 -*-
# 在杨辉三角中，每个数是它左上方和右上方的数的和。
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0:
        	return [1]
        if rowIndex == 1:
        	return [1,1]
        if rowIndex >1:
        	list = [[] for i in range(rowIndex+1)]
        	for i in range(rowIndex+1):
        		list[i] = [1 for j in range(i+1)]
        	for i in range(2,rowIndex+1):
        		for j in range(1,i):
        			list[i][j] = list[i-1][j-1] + list[i-1][j]
        	return list[rowIndex]
if __name__ == '__main__':
	print(Solution().getRow(3))
        