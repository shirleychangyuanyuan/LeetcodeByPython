# -*- coding:utf-8 -*-
# 给定一个整数，编写一个函数来判断它是否是 2 的幂次方。

class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n >0 and n & (n - 1) == 0
if __name__ == '__main__':
	print(Solution().isPowerOfTwo(2))