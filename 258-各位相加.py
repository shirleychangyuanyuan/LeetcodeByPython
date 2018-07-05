# -*- coding:utf-8 -*-
# 给定一个非负整数 num，反复将各个位上的数字相加，直到结果为一位数。

class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num == 0:
        	return 0
        else:
        	return 1 + (num-1)%9