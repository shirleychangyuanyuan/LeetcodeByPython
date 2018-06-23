# -*- coding:utf-8 -*-
# 给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。

# 说明：本题中，我们将空字符串定义为有效的回文串。
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        newString = [i.lower() for i in s if i.isalnum()]
        return newString == newString[::-1]
if __name__ == '__main__':
	print(Solution().isPalindrome("A man, a plan, a canal: Panama"))
	print(Solution().isPalindrome("race a car"))

