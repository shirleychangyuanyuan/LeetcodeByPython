# -*- coding:utf-8 -*-
#判断一个整数是否是回文数。不能使用辅助空间。正读反读都一样。负数不是回文数

class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False
        else:
            x = str(x)
            return x == x[::-1]
        #   return x == "".join(reversed(x))
s=Solution()
print s.isPalindrome(121)