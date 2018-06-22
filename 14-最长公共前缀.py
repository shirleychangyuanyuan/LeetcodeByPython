# -*- coding:utf-8 -*-
#编写一个函数来查找字符串数组中最长的公共前缀字符串。
#先找最短的字符串，然后再遍历这个字符串，与数组中的其他字符串比较，直到不相等，返回
class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        shortest=min(strs,key=len)#按长度取最小的那个字符串
        for i,ch in enumerate(shortest):
            for other in strs:
                if other[i] !=ch:
                    return shortest[:i]
        return shortest#要注意如果输入的是[""]，返回“”

