# -*- coding:utf-8 -*-


# 实现 strStr() 函数。

# 给定一个 haystack 字符串和一个 needle 字符串，
# 在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1。
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        n = len(haystack)
        m = len(needle)

        if m == 0:
        	return 0

        
        i = 0
        while i <= n - m :
            if haystack[i:i+m] == needle:
                return i
            i = i + 1    
        return -1


if __name__ == '__main__':
    print(Solution().strStr("abcdnfff", "dnfff"))
