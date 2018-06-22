# -*- coding:utf-8 -*-
# 给定一个仅包含大小写字母和空格 ' ' 的字符串，返回其最后一个单词的长度。

# 如果不存在最后一个单词，请返回 0 。

# 说明：一个单词是指由字母组成，但不包含任何空格的字符串。

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        list = s.split()
        # if list == []:
        # 	return 0
        # else:
        # 	return len(list[-1])
        return len(list[-1]) if list != [] else 0
        

if __name__ == '__main__':
	print(Solution().lengthOfLastWord("HelloworldHELLO"))
	print(Solution().lengthOfLastWord("abc a "))
	print(Solution().lengthOfLastWord(""))