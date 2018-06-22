# -*- coding:utf-8 -*-
#
#给定一个范围为 32 位 int 的整数，将其颠倒。

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x==0:
            return x
        else:
            x=str(x)
            if '-' in x:
                x=int('-'+"".join(reversed(x[1:])))
            else:

                x=int("".join(reversed(x)))
            if abs(x)>2**31:
                return 0
            else:
                return x
    def reverse2(self,x):
        s=str(x)
        if x>=0:
            res=int(s[::-1])
        else:
            res=int("-"+s[1:][::-1])
        return res