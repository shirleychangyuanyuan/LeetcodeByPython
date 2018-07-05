# -*- coding:utf-8 -*-
# 给定两个字符串 s 和 t，判断它们是否是同构的。

# 如果 s 中的字符可以被替换得到 t ，那么这两个字符串是同构的。

# 所有出现的字符都必须用另一个字符替换，同时保留字符的顺序。两个字符不能映射到同一个字符上，但字符可以映射自己本身。
# 你可以假设 s 和 t 具有相同的长度。
# class Solution(object):
#     def isIsomorphic(self, s, t):
#         """
#         :type s: str
#         :type t: str
#         :rtype: bool
#         """
        
#         def sub(s,t):
#         	dict = {}
#         	for i in range(len(s)):
#         		if s[i] not in dict:
#         			dict[s[i]] = t[i]
#         		else:
#         			if dict[s[i]] != t[i]:
#         				return False
#         	return True
#         return sub(s,t) and sub(t,s)

list =[12,56,78]
print(list[-1])