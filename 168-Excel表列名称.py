# -*- coding:utf-8 -*-
# 给定一个正整数，返回它在 Excel 表中相对应的列名称。
class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        result = ''
        while n:
        	result += chr((n -1)%26 + ord('A'))
        	n = (n -1)/26
        return result[::-1]
if __name__ == '__main__':
	print(Solution().convertToTitle(533))