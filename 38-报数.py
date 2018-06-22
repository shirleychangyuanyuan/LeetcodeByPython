# -*- coding:utf-8 -*-
# 报数序列是指一个整数序列，按照其中的整数的顺序进行报数，得到下一个数。其前五项如下：
# 1.     1
# 2.     11
# 3.     21
# 4.     1211
# 5.     111221
# 1 被读作  "one 1"  ("一个一") , 即 11。
# 11 被读作 "two 1s" ("两个一"）, 即 21。
# 21 被读作 "one 2",  "one 1" （"一个二" ,  "一个一") , 即 1211。

# 给定一个正整数 n ，输出报数序列的第 n 项。

# 注意：整数顺序将表示为一个字符串。

class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        nums = '1'
        for i in range(n-1):
            j = 0
            new_nums = ''
            while j < len(nums):
        	    count = 1
        	
        	    while j < len(nums)-1 and nums[j] == nums[j+1]:
        		   j = j+1
        		   count = count +1
        	    j = j + 1
        	    new_nums = new_nums + str(count) + nums[j-1]
            nums = new_nums

        return nums
if __name__ == '__main__':
	print(Solution().countAndSay(2))



