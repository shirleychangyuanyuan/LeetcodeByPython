# -*- coding:utf-8 -*-
# 给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的一个字母异位词。
# 你可以假设字符串只包含小写字母。

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
        	return False
        alpha = {}
        beta = {}
        for c in s:
        	alpha[c] = alpha.get(c,0) + 1
        for c in t:
        	beta[c] = beta.get(c,0) + 1
        return alpha == beta

    def isAnagram2(self,s,t):
    	return sorted(s) == sorted(t)
