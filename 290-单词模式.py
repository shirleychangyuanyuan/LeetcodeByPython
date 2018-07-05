# -*- coding:utf-8 -*-
# 给定一种 pattern(模式) 和一个字符串 str ，判断 str 是否遵循相同的模式。

# 这里的遵循指完全匹配，例如， pattern 里的每个字母和字符串 str 中的每个非空单词之间存在着双向连接的对应模式
# 你可以假设 pattern 只包含小写字母， str 包含了由单个空格分隔的小写字母。  
class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        words = str.split(" ")
        if len(pattern) != len(words):
        	return False
        def sub(s, t):
        	dict = {}
        	for i in range(len(s)):
        		if s[i] not in dict:
        			dict[s[i]] = t[i]
        		else:
        			if dict[s[i]] != t[i]:
        				return False
        	return True
        return sub(pattern, words) and sub(words, pattern)
        		

if __name__ == '__main__':
	pattern = "abba"
	strl = "dog cat cat dog"
	print(Solution().wordPattern(pattern, strl))