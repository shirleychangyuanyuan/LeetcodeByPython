# -*- coding:utf-8 -*-

# 给定一个Excel表格中的列名称，返回其相应的列序号。

class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        number = 0
        n = len(s) -1
        for i in range(len(s)):
        	number += (ord(s[i]) % 65 + 1)* 26**n 
        	n -= 1
        
        return number
if __name__ == '__main__':
	print(Solution().titleToNumber('BA'))
