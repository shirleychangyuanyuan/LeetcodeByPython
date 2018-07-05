# -*- coding:utf-8 -*-

# 编写一个程序判断给定的数是否为丑数。

# 丑数就是只包含质因数 2, 3, 5 的正整数。
# 说明：

# 1 是丑数。
# 输入不会超过 32 位有符号整数的范围: [−231,  231 − 1]。
class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
        	return False
        for i in [2, 3, 5]:
        	while num % i == 0:
        		num /= i

        return num == 1

if __name__ == '__main__':
	print(Solution().isUgly(14))
