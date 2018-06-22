# -*- coding:utf-8 -*-

# 给定两个二进制字符串，返回他们的和（用二进制表示）。
# 输入为非空字符串且只包含数字 1 和 0。
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        integer = int(a,2) + int(b,2)
        result = bin(integer)[2:]
        return result
if __name__ == '__main__':
	print(Solution().addBinary('11','1'))