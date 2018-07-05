# -*- coding:utf-8 -*-
# 给定一个整数 n，返回 n! 结果尾数中零的数量。
#说明: 你算法的时间复杂度应为 O(log n) 。
class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = 0
        while n >= 5:
        	n = n /5
        	result += n
        return result
if __name__ == '__main__':
	print(Solution().trailingZeroes(5))
