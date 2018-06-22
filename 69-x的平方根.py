# -*- coding:utf-8 -*-
# 实现 int sqrt(int x) 函数。
# 计算并返回 x 的平方根，其中 x 是非负整数。
# 由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        left = 0
        right = x
        while left < right:
        	mid = int((left + right)/2)
        	if x < mid **2:
        		right = mid
        	else:
        		left = mid + 1
        if left > 1:
        	return left - 1
        else:
        	return left
if __name__ == '__main__':
	print(Solution().mySqrt(19090))